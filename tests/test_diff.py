from gendiff.generate_diff import generate_diff
import pytest



res_js = open("tests/fixtures/result_js.txt").read()
res_nested = open("tests/fixtures/result_nested.txt").read()
res_plain = open("tests/fixtures/result_plain.txt").read()
res_json = open("tests/fixtures/result_json.txt").read()



def test_diff():
    path1 = "tests/fixtures/file.json"
    path2 = "tests/fixtures/file2.json"

    path3 = "tests/fixtures/file1.yml"
    path4 = "tests/fixtures/file2.yml"

    path5 = "tests/fixtures/nested1_j.json"
    path6 = "tests/fixtures/nested2_j.json"

    path7 = "tests/fixtures/nested1_y.yml"
    path8 = "tests/fixtures/nested2_y.yml"
    
    assert generate_diff(path1, path2, "stylish") == res_js[:-1]
    assert generate_diff(path3, path4, "stylish") == res_js[:-1]

    assert generate_diff(path5, path6, "stylish") == res_nested[:-1]
    assert generate_diff(path5, path6, "plain") == res_plain[:-1]
    assert generate_diff(path5, path6, "json") == res_json[:-1]

    assert generate_diff(path7, path8, "stylish") == res_nested[:-1]
    assert generate_diff(path7, path8, "plain") == res_plain[:-1]
    assert generate_diff(path7, path8, "json") == res_json[:-1] 

