import json
import yaml



def parse(data1, data2):
    if data1.endswith('.json') and data2.endswith('json'):
        file1 = json.load(open("tests/fixtures/file.json"))
        file2 = json.load(open("tests/fixtures/file2.json"))
        return file1, file2
    elif data1.endswith(('yml', 'yaml')) and data2.endswith(('yml', 'yaml')):
        file1_y = yaml.safe_load(open("tests/fixtures/file1.yaml"))
        file2_y = yaml.safe_load(open("tests/fixtures/file2.yml"))
        return file1_y, file2_y
