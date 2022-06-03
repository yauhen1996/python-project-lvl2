from gendiff.generate_diff import generate_diff
import pytest
import json


@pytest.fixture
def data1():
    file1 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file1.json"))
    return file1

def data2():
    file2 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json"))
    return file2


def test_generate(data1, data2):
    assert generate_diff('', '') == ''
    assert generate_diff({"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22","follow": false}, {"timeout": 20, "verbose": true, "host": "hexlet.io"}) == "{- follow: false  host: hexlet.io - proxy: 123.234.53.22 - timeout: 50 + timeout: 20 + verbose: true}"
