import json


def plain(arg):
    def call(on, parent=[]):
        res = []
        ADDED = "Property '{}' was added with value: {}"
        DELETED = "Property '{}' was removed"
        UPDATED = "Property '{}' was updated. From {} to {}"
        for key, val in on.items():
            parent.append(key)
            if val["type"] == "added":
                res.append(ADDED.format('.'.join(parent), to_string(val["value"])))
            elif val["type"] == "deleted":
                res.append(DELETED.format('.'.join(parent)))
            elif val["type"] == "changed":
                res.append(UPDATED.format('.'.join(parent), to_string(val["value_1"]), to_string(val["value_2"])))
            elif val["type"] == "nested":
                res.append(call(val["children"], parent))
            parent.pop()
        return '\n'.join(res)
    return call(arg)


def to_string(value):
    if isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, dict):
        result = '[complex value]'
    else:
        result = json.dumps(value)
    return result
