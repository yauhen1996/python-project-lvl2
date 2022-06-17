import re
import json


def stylish(arg):
    def call(on):
        res = {}
        for key, val in on.items():
            if val["type"] == "nested":
                res[f'{key}'] = call(val["children"])
            elif val["type"] == "added":
                res[f'+ {key}'] = val["value"]
            elif val["type"] == "deleted":
                res[f'- {key}'] = val["value"]
            elif val["type"] == "unchanged":
                res[f'{key}'] = val["value"]
            elif val["type"] == "changed":
                res[f'- {key}'] = val["value_1"]
                res[f'+ {key}'] = val["value_2"]
        return res
    data = call(arg)
    string = json.dumps(data, indent=4)
    clear = re.sub('\"|,', '', string)
    result = list(clear)
    for i, v in enumerate(result):
        if v == '+':
            del result[i - 1]
            del result[i - 2]
        elif v == '-':
            del result[i - 1]
            del result[i - 2]
    return ''.join(result)
