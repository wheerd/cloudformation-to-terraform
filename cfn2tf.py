import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4

from troposphere import AWSObject, AWSProperty
from troposphere.validators import positive_integer, boolean, double, integer
from troposphere.cloudwatch import MetricStat, Metric
from troposphere.logs import MetricFilter
from troposphere.ec2 import SecurityGroup, SecurityGroupEgress, SecurityGroupIngress


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


import_submodules('troposphere')


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])


cfnResourceTypes = {}

for cfnType in all_subclasses(AWSObject):
    if hasattr(cfnType, 'resource_type'):
        cfnResourceTypes[cfnType.resource_type] = cfnType


def MetricStatOverride(label, blockProps, props, outfile, path):
    convertBlock(
        'metric',
        {
            **blockProps,
            **Metric.props,
            'Metric': (None, None)
        }, {
            **props,
            **props['Metric'],
            'Metric': None
        },
        outfile,
        path
    )


def MetricFilterOverride(label, blockProps, props, outfile, path):
    convertBlock(
        label,
        {'Name': (str, None), **blockProps},
        {'Name': props['_NAME_'], **props},
        outfile,
        path
    )


def SecurityGroupOverride(label, blockProps, props, outfile, path):
    convertBlock(
        label,
        { **blockProps, 'SecurityGroupEgress': ([SecurityGroupEgress], False), 'SecurityGroupIngress': ([SecurityGroupIngress], False)},
        {**props},
        outfile,
        path
    )


cfnResourceTypeOverwrites = {
    MetricStat: MetricStatOverride,
    MetricFilter: MetricFilterOverride,
    SecurityGroup: SecurityGroupOverride
}

prop_name_overrides = {
    'AWS::CloudWatch::Alarm/Metrics': 'metric_query',
    'MetricTransformations/MetricNamespace': 'namespace',
    'MetricTransformations/MetricName': 'name',
    'MetricTransformations/MetricValue': 'value',
    'AWS::Logs::MetricFilter/FilterPattern': 'pattern'
}


class cfn_resource(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        # cfnResourceTypes[self.name] = f
        return f


def main():
    with open('test.json', encoding='utf-8') as json_file:
        with open('output/main.tf', 'w') as outfile:
            cfn = json.load(json_file)
            convertCfn(cfn, outfile)


def convertCfn(cfn, outfile):
    convertVariables(cfn['Parameters'], outfile)
    convertResources(cfn['Resources'], outfile)


def convertVariables(vars, outfile):
    for name, props in vars.items():
        outfile.write(f'variable "{name}" {{\n')
        tfType, defaultValue = getTerraformType(
            props["Type"], props.get("Default"))
        outfile.write(f'  type = {tfType}\n')
        if defaultValue is not None:
            outfile.write(f'  default = {defaultValue}\n')
        if 'Description' in props:
            outfile.write(
                f'  description = {escapeString(props["Description"])}\n')
        outfile.write(f'}}\n\n')


def convertResources(resources, outfile):
    for name, attributes in resources.items():
        resourceType = attributes['Type']
        props = attributes['Properties']

        if resourceType not in cfnResourceTypes:
            raise NotImplementedError(
                f'Resource type "{resourceType}" is not supported')

        convertResource(cfnResourceTypes[resourceType], name, props, outfile)


def convertResource(resource, name, props, outfile):
    label = f'resource "{cfn_resource_name_to_tf(resource.resource_type)}" "{name}"'
    if resource in cfnResourceTypeOverwrites:
        cfnResourceTypeOverwrites[resource](label, resource.props, {
                                            **props, '_NAME_': name}, outfile, [resource.resource_type])
    else:
        convertBlock(label, resource.props, props,
                     outfile, [resource.resource_type])


def get_prop_name_with_override(path):
    for i, _ in enumerate(path):
        subpath = '/'.join(path[i:])
        if subpath in prop_name_overrides:
            return prop_name_overrides[subpath]
    return camel_case_to_snake_case(path[-1])


def convertBlock(label, blockProps,  props, outfile, path):
    indent = '  ' * (len(path) - 1)
    outfile.write(f'\n{indent}{label} {{\n')
    for prop, (propType, _) in blockProps.items():
        value = props.get(prop)
        subpath = path + [prop]
        propName = get_prop_name_with_override(subpath)
        if value is not None:
            if isinstance(propType, list):
                if inspect.isclass(propType[0]) and issubclass(propType[0], (AWSProperty, AWSObject)):
                    if propName.endswith('s'):
                        propName = propName[:-1]
                    for subblock in value:
                        convertBlock(
                            propName, propType[0].props, subblock, outfile, subpath)
                else:
                    outfile.write(
                        f'{indent}  {propName} = {convertValue(value, propType)}\n')
            else:
                if propType in cfnResourceTypeOverwrites:
                    cfnResourceTypeOverwrites[propType](
                        propName, propType.props, value, outfile, subpath)
                elif inspect.isclass(propType) and issubclass(propType, (AWSProperty, AWSObject)):
                    convertBlock(propName, propType.props,
                                 value, outfile, subpath)
                elif propType is None:
                    pass
                else:
                    outfile.write(
                        f'{indent}  {propName} = {convertValue(value, propType)}\n')
    outfile.write(f'{indent}}}\n')


def convertValue(value, valueType):
    if valueType == str:
        return escapeString(value)
    elif isinstance(valueType, list):
        valueType = valueType[0]
        return f"[{', '.join(convertValue(x, valueType) for x in value)}]"
    elif valueType == list:
        return f"[{', '.join(convertValue(x, str) for x in value)}]"
    elif valueType == boolean:
        return str(value).lower()
    elif valueType in (integer, positive_integer, double):
        return str(value)
    elif inspect.isfunction(valueType):
        return escapeString(value)
    else:
        print(repr(valueType))
    return '// TODO'


cnf_name_translation = {
    "a_w_s_":  "aws_",
    'e_c2_': 'ec2_',
    "cloud_watch_":  "cloudwatch_",
    'aws_logs_': "aws_cloudwatch_log_",
    'aws_cloudwatch_alarm': 'aws_cloudwatch_metric_alarm'
}


cfn_name_pattern = re.compile(r'[^a-z0-9]+')


def cfn_resource_name_to_tf(name):
    translated_name = cfn_name_pattern.sub('_', camel_case_to_snake_case(name))
    return functools.reduce(lambda n, p: n.replace(*p), cnf_name_translation.items(), translated_name)


camel_case_pattern = re.compile(r'(?<!^)(?=[A-Z])')


def camel_case_to_snake_case(string):
    return camel_case_pattern.sub('_', string).lower()


def getTerraformType(cfnType, default):
    if cfnType == 'Number':
        return 'number', default
    if cfnType == 'List<Number>':
        if default is not None:
            default = f"[{default}]"
        return 'list(number)', default
    if cfnType == 'CommaDelimitedList' or cfnType.startswith('List<'):
        if default is not None:
            default = transformStringList(s.strip()
                                          for s in default.split(','))
        return 'list(string)', default
    if cfnType.startswith('AWS::SSM::'):
        raise NotImplementedError('AWS SSM Parameters are not supported')
    return 'string', escapeString(default)


def transformStringList(strlist):
    return f"[{', '.join(escapeString(s) for s in strlist)}]"


def escapeString(string):
    if string is None:
        return None
    if isinstance(string, dict):
        if 'Ref' in string:
            return f'var.{string["Ref"]}'
        else:
            return f'"" // TODO: Not supported yet {", ".join(string.keys())}'
            raise NotImplementedError(f'Unsupported string value: {string!r}')
    if '\n' in string:
        marker = f'EOT_{str(uuid4())[:8]}'
        return f'<<{marker}\n{string}\n{marker}'
    return '"' + string.translate(
        str.maketrans({
            "\"":  r"\\\"",
            "\\": r"\\",
            "\n": r"\\n",
            "\t": r"\\t"
        })
    ) + '"'


def stringAttribute(name, value, outfile):
    if value is not None:
        outfile.write(f'  {name} = {escapeString(value)}\n')


def numberAttribute(name, value, outfile):
    if value is not None:
        outfile.write(f'  {name} = {value}\n')


def booleanAttribute(name, value, outfile):
    if value is not None:
        outfile.write(f'  {name} = {value.lower()}\n')


def stringListAttribute(name, value, outfile):
    if value is not None:
        outfile.write(f'  {name} = {transformStringList(value)}\n')


def stringDictAttribute(name, entries, outfile):
    if entries is not None:
        outfile.write(f'  {name} = {{\n')
        for entry in entries:
            outfile.write(
                f'    {entry["Name"]} = {escapeString(entry["Value"])}\n')
        outfile.write(f'  }}\n')


@cfn_resource('AWS::CloudWatch::Alarm')
def ccfn_cw_alarm(name, props, outfile):
    outfile.write(f'resource "aws_cloudwatch_metric_alarm" "{name}" {{\n')
    booleanAttribute('actions_enabled', props.get('ActionsEnabled'), outfile)
    stringListAttribute('alarm_actions', props.get('AlarmActions'), outfile)
    stringAttribute('alarm_description', props.get(
        'AlarmDescription'), outfile)
    stringAttribute('alarm_name', props.get('AlarmName'), outfile)
    stringAttribute('comparison_operator', props.get(
        'ComparisonOperator'), outfile)
    numberAttribute('datapoints_to_alarm', props.get(
        'DatapointsToAlarm'), outfile)
    stringDictAttribute('dimensions', props.get('Dimensions'), outfile)
    stringAttribute('evaluate_low_sample_count_percentiles',
                    props.get('EvaluateLowSampleCountPercentile'), outfile)
    numberAttribute('evaluation_periods', props.get(
        'EvaluationPeriods'), outfile)
    stringAttribute('extended_statistic', props.get(
        'ExtendedStatistic'), outfile)
    stringListAttribute('insufficient_data_actions',
                        props.get('InsufficientDataActions'), outfile)
    stringAttribute('metric_name', props.get('MetricName'), outfile)
    stringAttribute('namespace', props.get('Namespace'), outfile)
    stringListAttribute('ok_actions', props.get('OKActions'), outfile)
    numberAttribute('period', props.get('Period'), outfile)
    stringAttribute('statistic', props.get('Statistic'), outfile)
    numberAttribute('threshold', props.get('Threshold'), outfile)
    stringAttribute('threshold_metric_id', props.get(
        'ThresholdMetricId'), outfile)
    stringAttribute('treat_missing_data', props.get(
        'TreatMissingData'), outfile)
    stringAttribute('unit', props.get('Unit'), outfile)
    for metric in props.get('Metrics', []):
        outfile.write('\n  metric_query {\n')
        stringAttribute('  expression', metric.get('Expression'), outfile)
        stringAttribute('  id', metric.get('Id'), outfile)
        stringAttribute('  label', metric.get('Label'), outfile)
        if 'MetricStat' in metric:
            stat = metric['MetricStat']
            outfile.write('\n    metric {\n')
            stringDictAttribute(
                '    dimensions', stat['Metric'].get('Dimensions'), outfile)
            stringAttribute('    metric_name',
                            stat['Metric'].get('MetricName'), outfile)
            stringAttribute('    namespace',
                            stat['Metric'].get('Namespace'), outfile)
            numberAttribute('    period', stat.get('Period'), outfile)
            stringAttribute('    stat', stat.get('Stat'), outfile)
            stringAttribute('    unit', stat.get('Unit'), outfile)
            outfile.write('    }\n')
        numberAttribute('  period', metric.get('Period'), outfile)
        booleanAttribute('  return_data', metric.get('ReturnData'), outfile)
        outfile.write('  }\n')
    outfile.write(f'}}\n\n')


@cfn_resource('AWS::Logs::MetricFilter')
def ccfn_logs_metric_filter(name, props, outfile):
    return
    outfile.write(f'resource "aws_cloudwatch_log_metric_filter" "{name}" {{\n')
    outfile.write(f'}}\n\n')


if __name__ == '__main__':
    main()
