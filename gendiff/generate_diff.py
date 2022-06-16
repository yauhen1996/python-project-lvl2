__all__ = ["generate_diff"]
from gendiff.parser import parse
from gendiff.diff import diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_


def generate_diff(file_1, file_2, format="stylish"):
    if format == "stylish":
        return stylish(diff(parse(file_1), parse(file_2)))
    elif format == "plain":
        return plain(diff(parse(file_1), parse(file_2)))
    elif format == "json":
        return json_(diff(parse(file_1), parse(file_2)))
    
