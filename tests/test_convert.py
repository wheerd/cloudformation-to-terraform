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
test_files = glob.glob(str(test_case_dir.joinpath('cases', '*', '*.template')))


@pytest.mark.parametrize("cfn_template", test_files, ids=lambda f: os.path.basename(os.path.dirname(f)))
def test_convert(cfn_template):
    folder = os.path.dirname(cfn_template)
    output_folder = pathlib.Path(folder).joinpath('actual')
    output_folder.mkdir(exist_ok=True)
    output_path = pathlib.Path(folder).joinpath('actual', 'main.tf')
    expected_path = pathlib.Path(folder).joinpath('expected', 'main.tf')
    with open(cfn_template, 'r', encoding='utf-8') as input_file:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            convert(input_file, output_file)
    with open(output_path, 'r', encoding='utf-8') as actual_file:
        actual_lines = actual_file.readlines()
    with open(expected_path, 'r', encoding='utf-8') as expected_file:
        expected_lines = expected_file.readlines()
    diff = ''.join(unified_diff(expected_lines, actual_lines, fromfile='expected', tofile='actual'))
    assert diff == ''