import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4
from util import import_submodules

import_submodules('spec')

from spec import CloudFormationEntityMeta, CloudFormationParameter, OutputWriter, CloudFormationTemplate


def main():
    with open('ElasticBeanstalk_Simple.template.json', encoding='utf-8') as json_file:
        with OutputWriter('output/main.tf') as writer:
            cfn = json.load(json_file)
            convertCfn(cfn, writer)


def convertCfn(cfn, writer):
    template = CloudFormationTemplate()
    convertVariables(cfn['Parameters'], template, writer)
    convertResources(cfn['Resources'], template, writer)
    template.write(writer)


def convertVariables(vars, template, writer):
    for name, props in vars.items():
        parameter = CloudFormationParameter(name, props)
        template.add(parameter)


def convertResources(resources, template, writer):
    for name, attributes in resources.items():
        resourceType = attributes['Type']

        if resourceType not in CloudFormationEntityMeta.mapping:
            raise NotImplementedError(
                f'Resource type "{resourceType}" is not supported')

        entity_cls = CloudFormationEntityMeta.mapping[resourceType]
        entity = entity_cls(name, attributes)
        template.add(entity)

if __name__ == '__main__':
    main()
