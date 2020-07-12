import json
import importlib
import pkgutil
import inspect
import re
import functools
import pathlib
import numpy
from uuid import uuid4
from fuzzywuzzy import process
from scipy.sparse import csr_matrix
from scipy.optimize import linear_sum_assignment

from cloudformation_to_terraform.util import camel_case_to_snake_case, snake_case_with_abbreviation_fix, import_submodules, topological_sort
from cloudformation_to_terraform.spec import CloudFormationEntityMeta, StringValueConverter, BasicValueConverter, primitive_type_converters
from _tf_spec import cf_to_tf_resource_mapping

class TypeDefinition(object):

    def __init__(self):
        self.spec = {}
        self.cls_name = ''
        self.entity_cls_name = ''

    def get_type(self, spec):
        if 'PrimitiveType' in spec and spec["PrimitiveType"] is not None:
            if spec["PrimitiveType"] in primitive_type_converters:
                return f'{primitive_type_converters[spec["PrimitiveType"]].__name__}()', 'property'
            return f'None # Unsupported primitive type "{spec["PrimitiveType"]}"', 'property'
        if 'Type' in spec and spec["Type"] is not None:
            if spec["Type"] == 'List':
                item_type, _ = self.get_type({'Type': spec.get('ItemType'), 'PrimitiveType': spec.get('PrimitiveItemType')})
                if item_type.startswith('AWS_'):
                    return item_type, 'repeated_block'
                return f'ListValueConverter({item_type})', 'property'
            if spec["Type"] == 'Map':
                item_type, _ = self.get_type({'Type': spec.get('ItemType'), 'PrimitiveType': spec.get('PrimitiveItemType')})
                return f'MapValueConverter({item_type})', 'property'
            if spec["Type"] == 'Tag':
                return 'ResourceTag()', 'property'
            if spec["Type"] == 'Json':
                return '"json"', 'property'
            property_cls_name = f'{self.entity_cls_name}_{spec["Type"]}'
            if property_cls_name == 'AWS_SSM_Association_ParameterValues':
                return 'ListValueConverter(StringValueConverter())', 'property'
            return property_cls_name, 'block'
        raise NotImplementedError('Unsupported type')

    def get_dependencies(self):
        dependant_types = set()
        if 'Properties' in self.spec:
            for prop_spec in self.spec['Properties'].values():
                other_type = prop_spec.get("Type")
                if other_type in ('List', 'Map'):
                    other_type = prop_spec.get('ItemType')
                if other_type is not None and other_type not in ('Tag', 'Json', 'AWSSSMAssociationParameterValues'):
                    dependant_types.add(f'{self.entity_cls_name}_{other_type}')
        return dependant_types

    @property
    def is_self_dependant(self):
        return self.cls_name in self.get_dependencies()


class ApproximateResourceTypeDefinition(TypeDefinition):
    def __init__(self, name, spec):
        self.name = name
        self.namespace = snake_case_with_abbreviation_fix(name.split('::')[1])
        self.cls_name = name.replace('::', '_')
        self.spec = spec
        self.entity_cls_name = self.cls_name
        self.terraform_resource = snake_case_with_abbreviation_fix(name.replace('::', '_')).replace('__', '_')

    def write(self, spec_file):
        spec_file.write(f'class {self.cls_name}(CloudFormationResource):\n')
        spec_file.write(f'  cfn_type = "{self.name}"\n')
        spec_file.write(f'  tf_type = "{self.terraform_resource}" # TODO: Most likely not working\n')
        attrs = self.spec.get('Attributes', {}).keys()
        ref = 'arn' if 'Arn' not in attrs else 'id'
        spec_file.write(f'  ref = "{ref}"\n')
        if len(attrs) > 0:
            spec_file.write(f'  attrs = {{\n')
            for attr in attrs:
                mapped_name = snake_case_with_abbreviation_fix(attr)
                spec_file.write(f'    "{attr}": "{mapped_name}",\n')
            spec_file.write(f'  }}\n')
        else:
            spec_file.write(f'  attrs = {{}}\n')
        spec_file.write(f'\n')
        spec_file.write(f'  def write(self, w):\n')
        spec_file.write(f'    with self.resource_block(w):\n')
        properties = list(self.spec['Properties'].items())
        for prop_name, prop_spec in properties:
            prop_type, meta_type = self.get_type(prop_spec)
            if meta_type != 'property':
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", {prop_type})\n')
            else:
                tf_prop_name = snake_case_with_abbreviation_fix(prop_name)
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", "{tf_prop_name}", {prop_type})\n')
        if not properties:
            spec_file.write(f'      pass\n')
        spec_file.write(f'\n\n')



class TerraformResourceTypeDefinition(TypeDefinition):
    def __init__(self, name, tf_name, spec, tf_spec):
        self.name = name
        self.namespace = snake_case_with_abbreviation_fix(name.split('::')[1])
        self.cls_name = name.replace('::', '_')
        self.spec = spec
        self.entity_cls_name = self.cls_name
        self.terraform_resource = tf_name
        self.tf_spec = tf_spec

        tf_props = [k for k, v in tf_spec['block']['attributes'].items()]
        tf_blocks = list(tf_spec['block'].get('block_types', {}).keys())
        possible_names = tf_props + tf_blocks
        self.tf_attrs = [k for k, v in tf_spec['block']['attributes'].items() if v.get('computed', False)]

        self.cf_attrs = spec.get('Attributes', {}).keys()
        self.property_names = generate_best_name_matches(sorted(spec['Properties'].keys()), possible_names, snake_case_with_abbreviation_fix, score_cutoff=90)
        self.attribute_names = generate_best_name_matches(sorted(self.cf_attrs), self.tf_attrs, snake_case_with_abbreviation_fix, score_cutoff=90)

    @property
    def ref(self):
        if 'Id' not in self.cf_attrs and 'id' in self.tf_attrs:
            return 'id'
        elif 'Arn' not in self.cf_attrs and 'arn' in self.tf_attrs:
            return 'arn'
        elif 'Name' not in self.cf_attrs and 'name' in self.tf_attrs:
            return 'name'
        else:
            if len(self.tf_attrs) == 1:
                return self.tf_attrs[0]
            elif len(self.tf_attrs) > 1:
                return ''
        return None

    def write(self, spec_file):
        spec_file.write(f'class {self.cls_name}(CloudFormationResource):\n')
        spec_file.write(f'  cfn_type = "{self.name}"\n')
        spec_file.write(f'  tf_type = "{self.terraform_resource}"\n')
        
        ref = self.ref
        comment = ' # TODO: Probably not the correct mapping' if ref not in ('arn', 'id', 'name') else ''
        if ref == '':
            spec_file.write(f'  ref = None # TODO: Could not determine the ref automatically\n')
        elif ref is not None:
            spec_file.write(f'  ref = "{ref}"{comment}\n')

        if len(self.cf_attrs) > 0:
            spec_file.write(f'  attrs = {{\n')
            for attr in self.cf_attrs:
                if attr in self.attribute_names:
                    mapped_name = self.attribute_names[attr]
                    spec_file.write(f'    "{attr}": "{mapped_name}",\n')
                else:
                    mapped_name = snake_case_with_abbreviation_fix(attr)
                    spec_file.write(f'    "{attr}": "{mapped_name}", # TODO: Probably not the correct mapping\n')
            remaining_tf_names = sorted(set(self.tf_attrs) - set(self.attribute_names.values()) - set([ref or '']))
            if len(remaining_tf_names) > 0:
                    spec_file.write(f'    # Additional TF attributes: {", ".join(remaining_tf_names)}\n')
            spec_file.write(f'  }}\n')
        else:
            remaining_tf_names = sorted(set(self.tf_attrs) - set([ref or '']))
            if len(remaining_tf_names) > 0:
                spec_file.write(f'  attrs = {{}} # Additional TF attributes: {", ".join(remaining_tf_names)}\n')
            else:
                spec_file.write(f'  attrs = {{}}\n')

        spec_file.write(f'\n')

        spec_file.write(f'  def write(self, w):\n')
        spec_file.write(f'    with self.resource_block(w):\n')
        properties = list(self.spec['Properties'].items())
        for prop_name, prop_spec in properties:
            prop_type, meta_type = self.get_type(prop_spec)
            if prop_name in self.property_names:
                tf_prop_name = self.property_names[prop_name]
                comment = ''
            else:
                tf_prop_name = snake_case_with_abbreviation_fix(prop_name)
                comment = ' # TODO: Probably not the correct mapping'
            if meta_type != 'property':
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", {prop_type}){comment}\n')
            else:
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", "{tf_prop_name}", {prop_type}){comment}\n')
        if not properties:
            spec_file.write(f'      pass\n')
        spec_file.write(f'\n\n')

class PropertyTypeDefinition(TypeDefinition):
    def __init__(self, name, spec):
        self.name = name
        self.entity = name.split('.')[0]
        self.tf_block_type = snake_case_with_abbreviation_fix(name.split('.', 1)[1])
        self.namespace = snake_case_with_abbreviation_fix(name.split('::')[1])
        self.cls_name = name.replace('::', '_').replace('.', '_')
        self.entity_cls_name = self.entity.replace('::', '_')
        self.spec = spec

    def write(self, spec_file):
        spec_file.write(f'class {self.cls_name}(CloudFormationProperty):\n')
        spec_file.write(f'  def write(self, w):\n')
        spec_file.write(f'    with w.block("{self.tf_block_type}"):\n')
        properties = list(self.spec.get('Properties', {}).items())
        for prop_name, prop_spec in properties:
            prop_type, meta_type = self.get_type(prop_spec)
            if meta_type != 'property':
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", {prop_type})\n')
            else:
                tf_prop_name = snake_case_with_abbreviation_fix(prop_name)
                spec_file.write(f'      self.{meta_type}(w, "{prop_name}", "{tf_prop_name}", {prop_type})\n')
        if not properties:
            spec_file.write(f'      pass\n')
        spec_file.write(f'\n\n')

def generate_best_name_matches(input_names, defined_names, input_mapper, score_cutoff=70):
    scores = csr_matrix((len(input_names), len(defined_names)), dtype=numpy.int8).toarray()

    for i, input_name in enumerate(input_names):
        potential_output_name = input_mapper(input_name)
        best_matches = process.extractBests(potential_output_name, defined_names, score_cutoff=score_cutoff)
        for match, score in best_matches:
            j = defined_names.index(match)
            scores[i, j] = -score

    best_row, best_col = linear_sum_assignment(scores)
    return {input_names[i]: defined_names[j] for i, j in zip(best_row, best_col) if scores[i,j] <= -score_cutoff}

def regenerate_resource_mapping():
    directory = pathlib.Path(__file__).parent.absolute()
    with open(f'{directory}/terraform-schema.json', encoding='utf-8') as json_file:
        spec = json.load(json_file)
        tf_schemas = spec['provider_schemas']['aws']['resource_schemas']

    with open(f'{directory}/CloudFormationResourceSpecification.json', encoding='utf-8') as json_file:
        cfn_spec = json.load(json_file)

    tf_block_names = sorted(tf_schemas.keys())
    cfn_resource_names = sorted(cfn_spec['ResourceTypes'].keys())

    def name_mapper(name):
        return snake_case_with_abbreviation_fix(name.replace('::', '_')).replace('__', '_')

    cfn_resource_matches = generate_best_name_matches(cfn_resource_names, tf_block_names, name_mapper, score_cutoff=85)

    with open(f'{directory}/_tf_spec.py', 'w', encoding='utf-8') as output_file:
        formatted_spec = repr(cfn_resource_matches).replace(",", ",\n").replace("{", "{\n").replace("}", "\n}")
        print(f'cf_to_tf_resource_mapping = {formatted_spec}', file=output_file)


def main():
    directory = pathlib.Path(__file__).parent.absolute()
    with open(f'{directory}/CloudFormationResourceSpecification.json', encoding='utf-8') as json_file:
        spec = json.load(json_file)

    with open(f'{directory}/terraform-schema.json', encoding='utf-8') as json_file:
        tf_schemas = json.load(json_file)['provider_schemas']['aws']['resource_schemas']

    definitions = {}
    for name, property_spec in spec['PropertyTypes'].items():
        if '::' in name:
            parts = name.split('::')
            namespace = snake_case_with_abbreviation_fix(parts[1])

            if namespace not in definitions:
                definitions[namespace] = []

            definitions[namespace].append(PropertyTypeDefinition(name, property_spec))

    for name, resource_spec in spec['ResourceTypes'].items():
        parts = name.split('::')
        namespace = snake_case_with_abbreviation_fix(parts[1])

        if namespace not in definitions:
            definitions[namespace] = []

        if name in cf_to_tf_resource_mapping:
            tf_name = cf_to_tf_resource_mapping[name]
            definition = TerraformResourceTypeDefinition(name, tf_name, resource_spec, tf_schemas[tf_name])
        else:
            definition = ApproximateResourceTypeDefinition(name, resource_spec)

        definitions[namespace].append(definition)

    for namespace, file_definitions in definitions.items():
        definitions_by_name = { definition.cls_name: definition for definition in file_definitions }
        dependencies = [(name, cls.get_dependencies()) for name, cls in definitions_by_name.items()]
        with open(f'{directory}/{namespace}.py', 'w', encoding='utf-8') as spec_file:
            spec_file.write('from . import *\n\n')
            for cls_name in topological_sort(dependencies):
                definitions_by_name[cls_name].write(spec_file)


if __name__ == '__main__':
    main()
