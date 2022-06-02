import json
import re


def generate_diff(f_1, f_2):
    file1 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file1.json"))
    file2 = json.load(open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json"))
    dict1 = {}
    dict2 = {}
    file_1 = file1.items()
    file_2 = file2.items()
    set_f = file_1 | file_2
    for item in list(set_f):
        if item in file_1 and item in file_2:
            dict1[f'  {item[0]}'] = item[1]
        if item in file_1 and item not in file_2:
            dict1[f'- {item[0]}'] = item[1]
        if item in file_2 and item not in file_1:
            dict2[f'+ {item[0]}'] = item[1]
    sort1 = sorted(dict1.items(), key=lambda x: x[0][2])
    sort2 = sorted(dict2.items(), key=lambda x: x[0][2])
    general = dict(sort1 + sort2)
    gen_sort = sorted(general.items(), key=lambda x: x[0][2])
    result = json.dumps(dict(gen_sort), indent=2)
    clear_result = re.sub('\"|,', '', result)
    return clear_result
