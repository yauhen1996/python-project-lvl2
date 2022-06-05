from gendiff.generate_diff import generate_diff
import json
import pytest
import re


@pytest.fixture
def data_1():
    file1 = json.load(open("home/yauhen1996/python-project-lvl2/tests/fixtures/file1.json"))
    return file1


@pytest.fixture
def data_2():
    file2 = json.load(open("home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json"))
    return file2


@pytest.fixture
def clear_res():
    data = json.load(open(("home/yauhen1996/python-project-lvl2/tests/fixtures/result.json")))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    return clear


def test_diff(data_1, data_2, clear_res):
    assert clear_res == generate_diff(data_1, data_2)
