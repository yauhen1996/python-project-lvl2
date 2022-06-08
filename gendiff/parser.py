import json
import yaml


def parse(path):
    data = str(path)
    if data.endswith('.json'):
        f = json.load(open(data))
        return f
    elif data.endswith(('.yml', '.yaml')):
        f2 = yaml.safe_load(open(data))
        return f2
