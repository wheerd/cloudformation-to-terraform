from uuid import uuid4
import inspect
import json
import functools
import re

class GlobalRef(object):
    def __init__(self, reference):
        self.reference = reference

class NoValue(object):
    def __init__(self):
        self.ref = None
        self.reference = 'null'

global_references = {
    'AWS::AccountId': GlobalRef('data.aws_caller_identity.current.account_id'),
    'AWS::Region': GlobalRef('data.aws_region.current.name'),
    'AWS::URLSuffix': GlobalRef('data.aws_partition.current.dns_suffix'),
    'AWS::Partition': GlobalRef('data.aws_partition.current.partition'),
    'AWS::NoValue': NoValue()
}

global_template = """
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_partition" "current" {}
data "aws_availability_zones" "all" {}
"""


class CloudFormationTemplate(object):
    def __init__(self):
        self.references = global_references.copy()
        self.variables = {}
        self.resources = {}
        self.outputs = {}
        self.conditions = {}
        self.mappings = {}

    def add(self, entity):
        if hasattr(entity, 'name'):
            if isinstance(entity, CloudFormationResource):
                self.resources[entity.name] = entity
            elif isinstance(entity, CloudFormationParameter):
                self.variables[entity.name] = entity
            elif isinstance(entity, CloudFormationCondition):
                self.conditions[entity.name] = entity
            elif isinstance(entity, CloudFormationMapping):
                self.mappings[entity.name] = entity
            self.references[entity.name] = entity
        entity.template = self

    def write(self, writer):
        writer.write_raw(global_template)
        if len(self.conditions) > 0:
            with writer.block('# Conditions\nlocals'):
                for condition in self.conditions.values():
                    condition.write(writer)
        if len(self.mappings) > 0:
            with writer.block('# Mappings\nlocals'):
                for mapping in self.mappings.values():
                    mapping.write(writer)
        for variable in self.variables.values():
            variable.write(writer)
        for resource in self.resources.values():
            resource.write(writer)

class CloudFormationEntityMeta(type):
    mapping = {}

    def __new__(cls, name, bases, attr):
        subclass = super(CloudFormationEntityMeta, cls).__new__(cls, name, bases, attr)
        if hasattr(subclass, 'cfn_type'):
            CloudFormationEntityMeta.mapping[subclass.cfn_type] = subclass
        return subclass

class CloudFormationEntityBase(metaclass=CloudFormationEntityMeta):
    def __init__(self, attributes, properties):
        self.template = None
        self.attributes = attributes
        self.properties = properties

    def write(self, outfile):
        raise NotImplementedError()

    def _get_value(self, cf_name):
        parts = cf_name.split('.')
        if cf_name.startswith('#'):
            value = getattr(self, parts.pop(0)[1:])
        elif cf_name.startswith('$'):
            value = self.attributes.get(parts.pop(0)[1:])
        else:
            value = self.properties.get(parts.pop(0))
        while value is not None and len(parts) > 0:
            value = value.get(parts.pop(0))
        return value


    def property(self, writer, cf_name, tf_name, converter):  
        value = self._get_value(cf_name)
        if value is not None:
            converted_value = converter.convert(self.template, value)
            if converted_value is not None:
                writer.write_line(f'{tf_name} = {converted_value}')
    
    def dict_property(self, writer, cf_name, tf_name, converter):  
        values = self._get_value(cf_name)
        if values is not None:
            with writer.block(f'{tf_name} = '):
                for entry in values:
                    value = converter.convert(self.template, entry['Value'])
                    writer.write_line(f'{entry["Name"]} = {value}')
    
    def block(self, writer, cf_name, property_cls):  
        value = self._get_value(cf_name) if cf_name is not None else self.properties
        if value is not None:
            entity = property_cls(value)
            entity.template = self.template
            entity.write(writer)
    
    def repeated_block(self, writer, cf_name, property_cls):  
        values = self._get_value(cf_name)
        if values is not None:
            if not isinstance(values, list):
                values = [values]
            for value in values:
                entity = property_cls(value)
                entity.template = self.template
                entity.write(writer)
      

class CloudFormationResource(CloudFormationEntityBase):
    cfn_type = None
    tf_type = None
    ref = None

    def __init__(self, name, attributes):
        self.name = name
        super().__init__(attributes, attributes.get('Properties', {}))
    
    def resource_block(self, writer):
        return writer.block(f'resource "{self.tf_type}" "{self.name}"')

    @property
    def reference(self):
        return f'{self.tf_type}.{self.name}.{self.ref}'

class CloudFormationProperty(CloudFormationEntityBase):
    def __init__(self, attributes):
        self.spec = attributes
        super().__init__(attributes, attributes)


class CloudFormationCondition(CloudFormationEntityBase):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
        super().__init__({}, {})

    def write(self, writer):
        converted_expression = BasicValueConverter().convert(self.template, self.expression)
        writer.write_line(f'cond_{self.name} = {converted_expression}')

    @property
    def reference(self):
        return f'local.cond_{self.name}'


class CloudFormationMapping(CloudFormationEntityBase):
    def __init__(self, name, mapping):
        self.name = name
        super().__init__({}, mapping)

    def write(self, writer):
        first_group = next(iter(self.properties.values()))
        first_value = next(iter(first_group.values()))
        if isinstance(first_value, str):
            value_converter = StringValueConverter()
        elif isinstance(first_value, list):
            value_converter = ListValueConverter(BasicValueConverter)
        else: 
            value_converter = BasicValueConverter()
        with writer.block(f'map_{self.name} ='):
            for group_name, group in self.properties.items():
                with writer.block(f'{group_name} ='):
                    for name, value in group.items():
                        converted_value = value_converter.convert(self.template, value)
                        writer.write_line(f'{name} = {converted_value}')
        
    @property
    def reference(self):
        return f'local.map_{self.name}'

class ResourceTag(CloudFormationProperty):
    def __init__(self):
        pass

class CloudFormationExpression(object):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.expr

class TerraformString(CloudFormationExpression):
    def __init__(self, string):
        super().__init__(escape_tf_string(string))
        self.raw_string = string

class ValueConverter(object):
    def convert(self, template, value):
        if value is None:
            return None
        value = self.evaluate(template, value, converter=self)
        return self.do_convert(template, value)

    def evaluate(self, template, value, converter=None):
        if isinstance(value, dict):
            if len(value) == 1:
                func, args = list(value.items())[0]
                if func in cfn_functions:
                    if isinstance(args, list):
                        return cfn_functions[func](template, converter, *args)
                    return cfn_functions[func](template, converter, args)
                elif '::' in func:
                    return CloudFormationExpression(f'"TODO: Not supported yet: {func}"')
            value_converter = converter.item_type if isinstance(converter, MapValueConverter) else None
            value = { k: self.evaluate(template, v, converter=value_converter) for k, v in value.items() }
            return value
        elif isinstance(value, list):
            value_converter = converter.item_type if isinstance(converter, ListValueConverter) else None
            value = [self.evaluate(template, v, converter=value_converter) for v in value]
            return value
        return value
    
    def do_convert(self, template, value):
        raise NotImplementedError()

def escape_tf_string(value):
    value = str(value)
    if '\n' in value:
        marker = f'EOT_{str(uuid4())[:8]}'
        return f'<<{marker}\n{value}\n{marker}'
    return '"' + raw_escape_tf_string(value) + '"'

def raw_escape_tf_string(value):
    return value.translate(
        str.maketrans({
            "\"":  r"\\\"",
            "\\": r"\\",
            "\n": r"\\n",
            "\t": r"\\t"
        })
    )

class StringValueConverter(ValueConverter):
    def do_convert(self, template, value):
        return TerraformString(value) if not isinstance(value, CloudFormationExpression) else value.expr

class CloudFormationJsonEncoder(json.JSONEncoder):
    expr_tokens = {}

    def default(self, obj):
        if isinstance(obj, CloudFormationExpression):
            placeholder = f'$${uuid4()}$$'
            self.expr_tokens[placeholder] = obj.expr
            return placeholder
        return super().default(obj)

class JsonValueConverter(ValueConverter):
    def convert(self, template, value):
        if value is None:
            return None
        value = self.evaluate(template, value)
        value = json.dumps(value, indent=2, cls=CloudFormationJsonEncoder)
        for placeholder, expr in CloudFormationJsonEncoder.expr_tokens.items():
            value = value.replace(f'"{placeholder}"', f'${{{expr}}}')
        return TerraformString(value)


class BasicValueConverter(ValueConverter):
    def do_convert(self, template, value):
        return CloudFormationExpression(str(value))


class ListValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, template, value):
        if isinstance(value, CloudFormationExpression):
            return value
        if not isinstance(value, list):
            value = [value]

        if inspect.isclass(self.item_type):
            converter = self.item_type()
            converted_values = [str(converter.convert(template, x)) for x in value]
            return  CloudFormationExpression(f"[{', '.join(converted_values)}]")

        return CloudFormationExpression(f"[{', '.join(str(self.item_type.convert(template, x)) for x in value)}]")

class MapValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, template, value):
        entries = [f"{x['Name']} = {self.item_type.convert(template, x['Value'])}" for x in value]
        return  CloudFormationExpression(f"{{{', '.join(entries)}}}")

def cloudformation_ref(template, converter, name):
    entity = template.references.get(name)
    if entity is None:
        raise AttributeError(f'Cannot find the reference "{name}"')
    return CloudFormationExpression(entity.reference)

def cloudformation_condition(template, converter, name):
    condition = template.conditions.get(name)
    if condition is None:
        raise AttributeError(f'Cannot find the condition "{name}"')
    return CloudFormationExpression(condition.reference)

def cloudformation_find_in_map(template, converter, name, group, key):
    mapping = template.mappings.get(name)
    if mapping is None:
        raise AttributeError(f'Cannot find the condition "{name}"')
    converter = StringValueConverter() if converter is None else converter
    group = converter.convert(template, group)
    key = converter.convert(template, key)
    return CloudFormationExpression(f'{mapping.reference}[{group}][{key}]')

def cloudformation_select(template, converter, index, expr):
    converter = StringValueConverter() if converter is None else converter
    expr = ListValueConverter(converter).convert(template, expr)
    index = BasicValueConverter().convert(template, index)
    return CloudFormationExpression(f'({expr})[{index}]')

def cloudformation_get_att(template, converter, name, attr):
    resource = template.resources.get(name)
    if resource is None:
        raise AttributeError(f'Cannot find the resource "{name}"')
    if attr not in resource.attrs:
        return CloudFormationExpression(f'"TODO: Unsupported attribute {attr} on {name}"')
    attr_name = resource.attrs[attr]
    return CloudFormationExpression(f'{resource.tf_type}.{name}.{attr_name}')

def cloudformation_if(template, converter, condition_name, true_expression, false_expression):
    condition = template.conditions.get(condition_name)
    if condition is None:
        raise AttributeError(f'Cannot find the condition "{condition_name}"')
    converter = BasicValueConverter() if converter is None else converter
    true_converted = converter.convert(template, true_expression)
    false_converted = converter.convert(template, false_expression)
    return CloudFormationExpression(f'{condition.reference} ? {true_converted} : {false_converted}')

def cloudformation_join(template, converter, delimiter, values):
    converted_delimiter = escape_tf_string(delimiter)
    converted_values = ListValueConverter(StringValueConverter).convert(template, values)
    return CloudFormationExpression(f'join({converted_delimiter}, {converted_values})')

def cloudformation_bin_op(operator, converter_override=None):
    def op(template, converter, left, right):
        converter = converter_override or (BasicValueConverter() if converter is None else converter)
        left = converter.convert(template, left)
        right = converter.convert(template, right)
        return CloudFormationExpression(f'({left} {operator} {right})')
    return op

def cloudformation_not(template, converter, expression):
    converter = BasicValueConverter() if converter is None else converter
    expression = converter.convert(template, expression)
    return CloudFormationExpression(f'!({expression})')

def cloudformation_simple_func(name, converter_override=None):
    def op(template, converter, *args):
        converter = converter_override or (BasicValueConverter() if converter is None else converter)
        args = [str(converter.convert(template, arg)) for arg in args]
        return CloudFormationExpression(f'{name}({", ".join(args)})')
    return op

def cloudformation_get_azs(template, converter, region):
    if region != '':
        return CloudFormationExpression(f'(\ndata.aws_availability_zones.all.names # TODO: check region filtering: {json.dumps(region)} \n)')
    return CloudFormationExpression(f'data.aws_availability_zones.all.names')

def cloudformation_sub(template, converter, string, sub=None):
    parts = re.split(r'\$\{([^}]+)\}', string)
    var_names = parts[1::2]
    if sub is None:
        sub = { name: { 'Ref': name } for name in var_names}
    converter = StringValueConverter()
    sub = { name: converter.convert(template, value) for name, value in sub.items()}
    result_string = '"'
    for i, part in enumerate(parts):
        if i % 2 == 0:
            result_string += raw_escape_tf_string(part)
        else:
            result_string += f'${{{sub[part]}}}' 
    result_string += '"'
    return CloudFormationExpression(result_string)

cfn_functions = {
    "Ref": cloudformation_ref,
    "Condition": cloudformation_condition,
    "Fn::GetAtt": cloudformation_get_att,
    "Fn::FindInMap": cloudformation_find_in_map,
    "Fn::Join": cloudformation_join,
    "Fn::If": cloudformation_if,
    "Fn::Or": cloudformation_bin_op('||'),
    "Fn::And": cloudformation_bin_op('&&'),
    "Fn::Equals": cloudformation_bin_op('==', StringValueConverter()),
    "Fn::Not": cloudformation_not,
    "Fn::Base64": cloudformation_simple_func('base64encode') ,
    "Fn::Split": cloudformation_simple_func('split') ,
    "Fn::Select": cloudformation_select,
    "Fn::GetAZs": cloudformation_get_azs,
    "Fn::Sub": cloudformation_sub
}

primitive_type_converters = {
    'String': StringValueConverter,
    'Json': JsonValueConverter,
    'Long': BasicValueConverter,
    'Integer': BasicValueConverter,
    'Double': BasicValueConverter,
    'Boolean': BasicValueConverter,
    'Timestamp': StringValueConverter
}

class CloudFormationParameter(CloudFormationEntityBase):
    def __init__(self, name, spec):
        self.name = name
        self.cfn_type = spec["Type"]
        self.tf_type, self.default_value = self.get_tf_type(self.cfn_type , spec.get("Default"))
        self.description = spec.get("Description")
        super().__init__(spec, {})
    
    def get_tf_type(self, cfn_type, default):
        if cfn_type == 'Number':
            return 'number', default
        if cfn_type == 'List<Number>':
            if default is not None:
                default = f"[{default}]"
            return 'list(number)', default
        if cfn_type == 'CommaDelimitedList' or cfn_type.startswith('List<'):
            if default is not None:
                values = [escape_tf_string(s.strip()) for s in default.split(',')]
                default = f"[{', '.join(values)}]"
            return 'list(string)', default
        if cfn_type.startswith('AWS::SSM::'):
            raise NotImplementedError('AWS SSM Parameters are not supported')
        return 'string', escape_tf_string(default)

    def write(self, writer):
        with writer.block(f'variable "{self.name}"'):
            writer.write_line(f'  type = {self.tf_type}')
            if self.default_value is not None:
                writer.write_line(f'  default = {self.default_value}')
            if self.description is not None:
                writer.write_line(f'  description = {escape_tf_string(self.description)}')

    @property
    def reference(self):
        return f'var.{self.name}'


class OutputWriter(object):
    def __init__(self, file_name=None, outfile=None):
        self.file_name = file_name
        self.indent_level = 0
        self.outfile = outfile

    def __enter__(self):
        self.outfile = open(self.file_name, 'w', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.outfile.close()

    def block(self, label):
        return IndentedBlock(self, label)

    def variable(self, name):
        return IndentedBlock(self, f'variable "{name}"')

    def write_line(self, line):
        self.outfile.write(self.indent + line + '\n')

    def write_raw(self, raw):
        self.outfile.write(raw)

    @property
    def indent(self):
        return '  ' * self.indent_level

class IndentedBlock(object):
    def __init__(self, writer, label):
        self.writer = writer
        self.label = label

    def __enter__(self):
        self.writer.write_line('')
        self.writer.write_line(f'{self.label} {{')
        self.writer.indent_level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.writer.indent_level -= 1
        self.writer.write_line('}')