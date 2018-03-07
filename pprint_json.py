import json
import sys


def load_json(file_with_json):
    with open(file_with_json, encoding='utf8') as json_string:
        return json.loads(json_string.read())


def print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    print_json(load_json(sys.argv[1]))