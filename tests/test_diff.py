#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest
import json
import yaml
import re
from gendiff.parser import parse



@pytest.fixture
def result():
    data = json.load(open("tests/fixtures/result.json"))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    return clear



def test_diff_json(result):
    path1 = "tests/fixtures/file.json"
    path2 = "tests/fixtures/file2.json"
    path3 = "tests/fixtures/file1.yaml"
    path4 = "tests/fixtures/file2.yml"

    assert generate_diff(path1, path2) == result
    assert generate_diff(path3, path4) == result


