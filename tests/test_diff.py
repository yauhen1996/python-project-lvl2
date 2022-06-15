#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest
import json
from gendiff.parser import parse
from gendiff.diff import diff
from gendiff.format.stylish import stylish



@pytest.fixture
def result_plain():
    res1 = open("tests/fixtures/result_plain.txt").read()
    return res1 



@pytest.fixture
def result_nested():
    res2 = open("tests/fixtures/result_nested.txt").read()
    return res2


def test_diff_json(result_plain, result_nested):
    path1 = "tests/fixtures/file.json"
    path2 = "tests/fixtures/file2.json"
    path3 = "tests/fixtures/file1.yaml"
    path4 = "tests/fixtures/file2.yml"
    path5 = "tests/fixtures/nested1_j.json"
    path6 = "tests/fixtures/nested2_j.json"
    path7 = "tests/fixtures/nested1_y.yml"
    path8 = "tests/fixtures/nested2_y.yml"
    
    assert generate_diff(path1, path2) == result_plain[:-1]
    assert generate_diff(path3, path4) == result_plain[:-1]
    assert generate_diff(path5, path6) == result_nested[:-1]
    assert generate_diff(path7, path8) == result_nested[:-1]

