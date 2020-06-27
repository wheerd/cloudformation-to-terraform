import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4
from util import import_submodules

import_submodules('spec')

from spec import CloudFormationEntityMeta, CloudFormationParameter


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
        parameter = CloudFormationParameter(name, props)
        parameter.write(outfile)


def convertResources(resources, outfile):
    for name, attributes in resources.items():
        resourceType = attributes['Type']

        if resourceType not in CloudFormationEntityMeta.mapping:
            raise NotImplementedError(
                f'Resource type "{resourceType}" is not supported')

        entity_cls = CloudFormationEntityMeta.mapping[resourceType]
        entity = entity_cls(name, attributes)

        entity.write(outfile)

if __name__ == '__main__':
    main()
