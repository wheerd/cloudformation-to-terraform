# -*- coding: utf-8 -*-

import pathlib
import glob
import os
import pytest
from difflib import unified_diff
from cloudformation_to_terraform.main import convert

__author__ = "wheerd"
__copyright__ = "wheerd"
__license__ = "mit"

test_case_dir = pathlib.Path(__file__).parent.absolute()
test_files = glob.glob(str(test_case_dir.joinpath('cases', '*.template')))


@pytest.mark.parametrize("cfn_template", test_files, ids=os.path.basename)
def test_convert(cfn_template):
    with open(cfn_template, 'r', encoding='utf-8') as input_file:
        with open(cfn_template + '.tf', 'w', encoding='utf-8') as output_file:
            convert(input_file, output_file)
    with open(cfn_template + '.tf', 'r', encoding='utf-8') as actual_file:
        actual_lines = actual_file.readlines()
    with open(cfn_template + '.expected.tf', 'r', encoding='utf-8') as expected_file:
        expected_lines = expected_file.readlines()
    diff = ''.join(unified_diff(actual_lines, expected_lines, fromfile=cfn_template + '.tf', tofile=cfn_template + 'expected.tf'))
    assert diff == ''