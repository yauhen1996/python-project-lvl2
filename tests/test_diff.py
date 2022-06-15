#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest



@pytest.fixture
def result_plain():
    res1 = open("tests/fixtures/result_plain.txt").read()
    return res1 



@pytest.fixture
def result_nested():
    res2 = open("tests/fixtures/result_nested.txt").read()
    return res2



@pytest.fixture
def result_json():
    res3 = open("tests/fixtures/result_json.txt").read()
    return res3



@pytest.fixture
def result_js():
    res4 = open("tests/fixtures/result_json.txt").read()
    return res4



def test_diff_json(result_plain, result_nested, result_json, result_js):
    path1 = "tests/fixtures/file.json"
    path2 = "tests/fixtures/file2.json"
    path3 = "tests/fixtures/file1.yaml"
    path4 = "tests/fixtures/file2.yml"
    path5 = "tests/fixtures/nested1_j.json"
    path6 = "tests/fixtures/nested2_j.json"
    path7 = "tests/fixtures/nested1_y.yml"
    path8 = "tests/fixtures/nested2_y.yml"
    

    assert generate_diff(path5, path6, format="stylish") == result_nested[:-1]
    assert generate_diff(path5, path6, format="plain") == result_plain[:-1]
    assert generate_diff(path5, path6, format="json") == result_json[:-1]

    assert generate_diff(path7, path8, format="stylish") == result_nested[:-1]
    assert generate_diff(path7, path8, format="plain") == result_plain[:-1]
    assert generate_diff(path7, path8, format="json") == result_json[:-1] 

