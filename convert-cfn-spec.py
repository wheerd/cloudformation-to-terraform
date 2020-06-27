import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4

from util import camel_case_to_snake_case, snake_case_with_abbreviation_fix, import_submodules, topological_sort

from spec import CloudFormationEntityMeta, StringValueConverter, BasicValueConverter, primitive_type_converters

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


class ResourceTypeDefinition(TypeDefinition):
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
        spec_file.write(f'  tf_type = "{self.terraform_resource}"\n')
        spec_file.write(f'  ref = "arn"\n')
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


def main():
    with open('CloudFormationResourceSpecification.json', encoding='utf-8') as json_file:
        spec = json.load(json_file)

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

            definitions[namespace].append(ResourceTypeDefinition(name, resource_spec))

        for namespace, file_definitions in definitions.items():
            definitions_by_name = { definition.cls_name: definition for definition in file_definitions }
            dependencies = [(name, cls.get_dependencies()) for name, cls in definitions_by_name.items()]
            with open(f'generated-spec/{namespace}.py', 'w', encoding='utf-8') as spec_file:
                spec_file.write('from . import *\n\n')
                for cls_name in topological_sort(dependencies):
                    definitions_by_name[cls_name].write(spec_file)


if __name__ == '__main__':
    main()
