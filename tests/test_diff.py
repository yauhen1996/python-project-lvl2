#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest



res_js = open("tests/fixtures/result_js.txt").read()
res_nested = open("tests/fixtures/result_nested.txt").read()
res_plain = open("tests/fixtures/result_plain.txt").read()
res_json = open("tests/fixtures/result_json.txt").read()



def test_diff_json():
    path1 = "tests/fixtures/file.json"
    path2 = "tests/fixtures/file2.json"

    path3 = "tests/fixtures/file1.yaml"
    path4 = "tests/fixtures/file2.yml"

    path5 = "tests/fixtures/nested1_j.json"
    path6 = "tests/fixtures/nested2_j.json"

    path7 = "tests/fixtures/nested1_y.yml"
    path8 = "tests/fixtures/nested2_y.yml"
    
    assert generate_diff(path1, path2, format="stylish") == res_js[:-1]

    assert generate_diff(path5, path6, format="stylish") == res_nested[:-1]
    assert generate_diff(path5, path6, format="plain") == res_plain[:-1]
    assert generate_diff(path5, path6, format="json") == res_json[:-1]

    assert generate_diff(path7, path8, format="stylish") == res_nested[:-1]
    assert generate_diff(path7, path8, format="plain") == res_plain[:-1]
    assert generate_diff(path7, path8, format="json") == res_json[:-1] 

