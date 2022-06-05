#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import json
import pytest
import re
import os


@pytest.fixture
def clear_res():
    data = json.load(open(("/home/yauhen1996/python-project-lvl2/tests/fixtures/result.json")))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    return clear


@pytest.fixture
def data_2():
    file_2 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json"))
    return file_2


@pytest.fixture
def data_1():
    file_1 = json.load(open(os.path.abspath('file.json')))
    return file_1


def test_diff(data_1, data_2, clear_res):
    assert clear_res == generate_diff(data_1, data_2)
