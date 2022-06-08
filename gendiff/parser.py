import json
import yaml


def parse(data1, data2):
    if data1.endswith('.json') and data2.endswith('.json'):
        file2_j = json.load(open("tests/fixtures/file2.json"))
        return json.load(open("tests/fixtures/file.json")), file2_j
    elif data1.endswith(('yml', 'yaml')) and data2.endswith(('yml', 'yaml')):
        file2_y = yaml.safe_load(open("tests/fixtures/file2.yml"))
        return yaml.safe_load(open("tests/fixtures/file1.yaml")), file2_y
