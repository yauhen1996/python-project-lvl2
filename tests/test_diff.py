#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
import pytest




def test_diff():
    import json
    import re
    data = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/result.json"))
    result = json.dumps(dict(data), indent=2)
    clear = re.sub('\"|,', '', result)
    file_1 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file.json"))
    file_2 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json"))
    assert clear == generate_diff(file_1, file_2)
