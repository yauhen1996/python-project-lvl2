import json
import itertools


def generate_diff(f_1, f_2):
    with open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file1.json") as f:
        file1 = json.load(f)
    with open("/home/yauhen1996/python-project-lvl2/tests/fixtures/file2.json") as f:
        file2 = json.load(f)
    f1 = file1.items()
    f2 = file2.items()
    l = []
    for k1, v1 in f1:
        for k2, v2 in f2:
            if (k1, v1) in f2:
                l.append(f'  {k1}: {v1}')
            if k1 in (k2, v2) and v1 not in (k2, v2):
                l.extend([f'+ {k2}: {v2}'])
                l.extend([f'- {k1}: {v1}'])
            if (k1, v1) not in f2:
                l.extend([f'- {k1}: {v1}'])
            if (k2, v2) not in f1:
                l.extend([f'+ {k2}: {v2}'])
    del_repeat = list(set(l))
    del_repeat.sort(key=lambda x: x[2])                         
    build = itertools.chain("{", del_repeat, "}")
    result = '\n'.join(build)
    return result
