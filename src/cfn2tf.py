import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4
from util import import_submodules

import_submodules('spec')

from spec import CloudFormationEntityMeta, CloudFormationParameter, OutputWriter, CloudFormationTemplate, CloudFormationCondition, CloudFormationMapping


def main():
    with open('ElasticBeanstalk_Simple.template.json', encoding='utf-8') as json_file:
        with OutputWriter('output/main.tf') as writer:
            cfn = json.load(json_file)
            convert_cloudformation(cfn, writer)


def convert_cloudformation(cfn, writer):
    template = CloudFormationTemplate()
    convert_mappings(cfn.get('Mappings', {}), template)
    convert_conditions(cfn.get('Conditions', {}), template)
    convert_variables(cfn['Parameters'], template, writer)
    convert_resources(cfn['Resources'], template, writer)
    template.write(writer)


def convert_conditions(conditions, template):
    for name, expression in conditions.items():
        template.add(CloudFormationCondition(name, expression))


def convert_mappings(mappings, template):
    for name, mapping in mappings.items():
        template.add(CloudFormationMapping(name, mapping))


def convert_variables(vars, template, writer):
    for name, props in vars.items():
        template.add(CloudFormationParameter(name, props))


def convert_resources(resources, template, writer):
    for name, attributes in resources.items():
        resource_type = attributes['Type']

        if resource_type not in CloudFormationEntityMeta.mapping:
            raise NotImplementedError(
                f'Resource type "{resource_type}" is not supported')

        entity_cls = CloudFormationEntityMeta.mapping[resource_type]
        entity = entity_cls(name, attributes)
        template.add(entity)

if __name__ == '__main__':
    main()
