import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf8') as json_data:
        return json.loads(json_data.read())


def pretty_print_json(data):
    j = json.dumps(data, indent=4, ensure_ascii=False)
    print(j)
    return j


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))