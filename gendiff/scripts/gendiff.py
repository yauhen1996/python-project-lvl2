#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff
from gendiff.parser import parse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    file1, file2 = parse(args.first_file, args.second_file)
    print(generate_diff(file1, file2))
    


if __name__ == '__main__':
    main()
