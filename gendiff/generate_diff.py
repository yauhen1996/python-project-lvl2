from gendiff.parser import parse
from gendiff.diff import diff
from gendiff.format.stylish import stylish


def generate_diff(data_1, data_2, format="stylish"):
    file_1 = parse(data_1)
    file_2 = parse(data_2)
    if format == "stylish":
        return stylish(diff(file_1, file_2))
    
