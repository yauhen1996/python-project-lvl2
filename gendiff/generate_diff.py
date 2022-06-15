from gendiff.parser import parse
from gendiff.diff import diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_


def generate_diff(data_1, data_2, format="stylish"):
    file_1 = parse(data_1)
    file_2 = parse(data_2)
    if format == "stylish":
        return stylish(diff(file_1, file_2))
    elif format == "plain":
        return plain(diff(file_1, file_2))
    elif format == "json":
        return json_(diff(file_1, file_2))
    
