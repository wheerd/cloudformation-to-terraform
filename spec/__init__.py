from uuid import uuid4
import inspect

class CloudFormationEntityMeta(type):
    mapping = {}

    def __new__(cls, name, bases, attr):
        subclass = super(CloudFormationEntityMeta, cls).__new__(cls, name, bases, attr)
        if hasattr(subclass, 'resource_type'):
            CloudFormationEntityMeta.mapping[subclass.resource_type] = subclass
        return subclass

class CloudFormationEntityBase(metaclass=CloudFormationEntityMeta):
    def write(self, outfile):
        raise NotImplementedError()

    def write_block(self, label, outfile, path):
        indent = '  ' * (len(path) - 1)
        outfile.write(f'\n{indent}{label} {{\n')
        if hasattr(self, 'props') and 'Properties' in self.spec:
            for prop, (converter, tf_name) in self.props.items():
                value = self.spec['Properties'].get(prop)
                subpath = path + [prop]
                if inspect.isclass(converter):
                    converter = converter()
                converted_value = converter.convert(value)
                if converted_value is not None:
                    if tf_name is None:
                        outfile.write(f'{indent}  {converted_value}\n')
                    else:
                        outfile.write(f'{indent}  {tf_name} = {converted_value}\n')
        outfile.write(f'{indent}}}\n')

class CloudFormationResource(CloudFormationEntityBase):
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec

    def write(self, outfile):
        label = f'resource "{self.terraform_resource}" "{self.name}"'
        self.write_block(label, outfile, [self.name])

class CloudFormationProperty(CloudFormationEntityBase):
    def convert(self, value):
        if value is None:
            return None
        output = f'\n{self.tf_block_type} {{\n'
        if hasattr(self, 'props'):
            for prop, (converter, tf_name) in self.props.items():
                prop_value = value.get(prop)
                if inspect.isclass(converter):
                    converter = converter()
                converted_value = converter.convert(prop_value)
                if converted_value is not None:
                    if tf_name is None:
                        output += f'{converted_value}\n'
                    else:
                        output += f'{tf_name} = {converted_value}\n'
        output += f'}}\n'
        return output

class ResourceTag(CloudFormationProperty):
    def __init__(self):
        pass

class ValueConverter(object):
    def convert(self, value):
        if value is None:
            return None
        if isinstance(value, dict):
            if 'Ref' in value:
                return f'var.{value["Ref"]}'
            else:
                return f'"" // TODO: Not supported yet {", ".join(value.keys())}'
        return self.do_convert(value)
    
    def do_convert(self, value):
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
    def do_convert(self, value):
        return escape_tf_string(value)

class BasicValueConverter(ValueConverter):
    def do_convert(self, value):
        return str(value)


class ListValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, value):
        if inspect.isclass(self.item_type):
            converted_values = [self.item_type().convert(x) for x in value]
            return f"[{', '.join(converted_values)}]"

        return f"[{', '.join(self.item_type.convert(x) for x in value)}]"

class BlockValueConverter(ValueConverter):
    def __init__(self, block_type):
        self.block_type = block_type() if inspect.isclass(block_type) else block_type

    def do_convert(self, value):
        converted_values = [self.block_type.convert(x) for x in value]
        return '\n\n'.join(converted_values)

class MapValueConverter(ValueConverter):
    def __init__(self, item_type):
        self.item_type = item_type

    def do_convert(self, value):
        entries = [f"{x['Name']} = {self.item_type.convert(x['Value'])}" for x in value]
        return f"{{{', '.join(entries)}}}"

primitive_type_converters = {
    'String': StringValueConverter,
    'Json': StringValueConverter,
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
        self.tf_type, self.default_value = self.getTerraformType(self.cfn_type , spec.get("Default"))
        self.description = spec.get("Description")
    
    def getTerraformType(self, cfnType, default):
        if cfnType == 'Number':
            return 'number', default
        if cfnType == 'List<Number>':
            if default is not None:
                default = f"[{default}]"
            return 'list(number)', default
        if cfnType == 'CommaDelimitedList' or cfnType.startswith('List<'):
            if default is not None:
                values = [escape_tf_string(s.strip()) for s in default.split(',')]
                default = f"[{', '.join(values)}]"
            return 'list(string)', default
        if cfnType.startswith('AWS::SSM::'):
            raise NotImplementedError('AWS SSM Parameters are not supported')
        return 'string', escape_tf_string(default)

    def write(self, outfile):
        outfile.write(f'variable "{self.name}" {{\n')
        outfile.write(f'  type = {self.tf_type}\n')
        if self.default_value is not None:
            outfile.write(f'  default = {self.default_value}\n')
        if self.description is not None:
            outfile.write(f'  description = {escape_tf_string(self.description)}\n')
        outfile.write(f'}}\n\n')