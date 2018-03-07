import json
import sys


def load_json(json_file):
    with open(json_file, encoding='utf8') as jdata:
        return json.loads(jdata.read())


def print_json(json_data):
    j = json.dumps(json_data, indent=4, ensure_ascii=False)
    print(j)
    return j


if __name__ == '__main__':
    print_json(load_json(sys.argv[1]))