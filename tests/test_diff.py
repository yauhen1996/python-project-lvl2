#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest
import json
import re


@pytest.fixture
def data_1():
    file_1 = json.load(open("tests/fixtures/file.json"))
    return file_1



@pytest.fixture
def data_2():
    file_2 = json.load(open("tests/fixtures/file2.json"))
    return file_2


@pytest.fixture
def clear_result():
    data = json.load(open("tests/fixtures/result.json"))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    return clear


def test_diff(data_1, data_2, clear_result):
    assert clear_result == generate_diff(data_1, data_2)
