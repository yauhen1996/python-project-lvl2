import json
import re


def generate_diff(f_1, f_2):
    dict1 = {}
    dict2 = {}
    file1 = f_1.items()
    file2 = f_2.items()
    set_f = file1 | file2
    for item in list(set_f):
        if item in file1 and item in file2:
            dict1[f'  {item[0]}'] = item[1]
        elif item in file1 and item not in file2:
            dict1[f'- {item[0]}'] = item[1]
        else:
            dict2[f'+ {item[0]}'] = item[1]
    sort1 = sorted(dict1.items(), key=lambda x: x[0][2])
    sort2 = sorted(dict2.items(), key=lambda x: x[0][2])
    general = dict(sort1 + sort2)
    gen_sort = sorted(general.items(), key=lambda x: x[0][2])
    result = json.dumps(dict(gen_sort), indent=2)
    clear_result = re.sub('\"|,', '', result)
    return clear_result
