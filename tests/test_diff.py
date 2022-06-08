#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest
import json
import yaml
import re


@pytest.fixture
def data_j():
    file1_j = json.load(open("tests/fixtures/file.json"))
    file2_j = json.load(open("tests/fixtures/file2.json"))
    return file1_j, file2_j


@pytest.fixture
def data_y():
    with open("tests/fixtures/file1.yaml") as f:
        file1_y = yaml.safe_load(f)
    with open("tests/fixtures/file2.yml") as f:
        file2_y = yaml.safe_load(f)
    return file1_y, file2_y



@pytest.fixture
def result():
    data = json.load(open("tests/fixtures/result.json"))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    return clear



def test_diff_json(data_j, data_y, result):
    data1_j, data2_j = data_j
    data1_y, data2_y = data_y
    assert result == generate_diff(data1_j, data2_j)
    assert result == generate_diff(data1_y, data2_y)


