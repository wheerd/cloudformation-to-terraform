from uuid import uuid4
import inspect
import json
import functools


class CloudFormationTemplate(object):
    def __init__(self):
        self.references = {}
        self.variables = {}
        self.resources = {}
        self.outputs = {}

    def add(self, entity):
        if hasattr(entity, 'name'):
            if isinstance(entity, CloudFormationResource):
                self.resources[entity.name] = entity
            elif isinstance(entity, CloudFormationParameter):
                self.variables[entity.name] = entity
            self.references[entity.name] = entity
        entity.template = self

    def write(self, writer):
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

class ResourceTag(CloudFormationProperty):
    def __init__(self):
        pass

class CloudFormationExpression(object):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.expr

class ValueConverter(object):
    def convert(self, template, value):
        if value is None:
            return None
        value = self.evaluate(template, value)
        return self.do_convert(template, value)

    def evaluate(self, template, value):
        if isinstance(value, dict):
            if len(value) == 1:
                func, args = list(value.items())[0]
                if func == 'Ref':
                    entity = template.references.get(args)
                    if entity is None:
                        raise AttributeError(f'Cannot find the reference "{args}"')
                    return CloudFormationExpression(entity.reference)
                elif '::' in func:
                    return CloudFormationExpression(f'"TODO: Not supported yet: {func}"')
            value = { k: self.evaluate(template, v) for k, v in value.items() }
            return value
        elif isinstance(value, list):
            value = [self.evaluate(template, v) for v in value]
            return value
        return value
    
    def do_convert(self, template, value):
        raise NotImplementedError()

def escape_tf_string(value):
    value = str(value)
    if '\n' in value:
        marker = f'EOT_{str(uuid4())[:8]}'
        return f'<<{marker}\n{value}\n{marker}'
    return '"' + value.translate(
        str.maketrans({
            "\"":  r"\\\"",
            "\\": r"\\",
            "\n": r"\\n",
            "\t": r"\\t"
        })
    ) + '"'

class StringValueConverter(ValueConverter):
    def do_convert(self, template, value):
        return escape_tf_string(value) if not isinstance(value, CloudFormationExpression) else value.expr

class CloudFormationJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CloudFormationExpression):
            return obj.expr
        return super().default(obj)

class JsonValueConverter(ValueConverter):

    def convert(self, template, value):
        if value is None:
            return None
        value = self.evaluate(template, value)
        value = json.dumps(value, indent=2, cls=CloudFormationJsonEncoder)
        return escape_tf_string(value)


class BasicValueConverter(ValueConverter):
    def do_convert(self, template, value):
        return str(value)


class ListValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, template, value):
        if not isinstance(value, list):
            value = [value]

        if inspect.isclass(self.item_type):
            converted_values = [self.item_type().convert(template, x) for x in value]
            return f"[{', '.join(converted_values)}]"

        return f"[{', '.join(self.item_type.convert(template, x) for x in value)}]"

class MapValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, template, value):
        entries = [f"{x['Name']} = {self.item_type.convert(template, x['Value'])}" for x in value]
        return f"{{{', '.join(entries)}}}"

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
    def __init__(self, file_name):
        self.file_name = file_name
        self.indent_level = 0
        self.outfile = None

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