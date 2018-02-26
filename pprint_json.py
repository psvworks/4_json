import json


def load_data(filepath):
    with open(filepath, encoding='utf8') as json_data:
        return json_data.read()


def pretty_print_json(data):
    j = json.loads(data)
    print(j)
    #print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))
    pass


if __name__ == '__main__':
    #p = "https:\\devman.org\media\filer_public\1d\32\1d32132e-efa4-4a6c-bd32-312acc3710ad\alco_shops.json"
    p = "alco_shops.json"
    pretty_print_json(load_data(p))
