# -*- coding: utf-8 -*-
"""
Cloudformation to Terraform converter
"""

import argparse
import sys
import logging

import json
import importlib
import pkgutil
import inspect
import re
import functools
from uuid import uuid4
from util import import_submodules

import_submodules('cloudformation_to_terraform.spec')

from cloudformation_to_terraform.spec import CloudFormationEntityMeta, CloudFormationParameter, OutputWriter, CloudFormationTemplate, CloudFormationCondition, CloudFormationMapping
from cloudformation_to_terraform import __version__

__author__ = "wheerd"
__copyright__ = "wheerd"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def convert(input_file, output_file):
    writer = OutputWriter(outfile=output_file)
    cfn = json.load(input_file)
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

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Cloudformation to Terrafrom converter")
    parser.add_argument(
        "--version",
        action="version",
        version="cf2tf {ver}".format(ver=__version__))
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting conversion...")
    convert(args.input_file, args.output_file)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
