# Prettify JSON

The script processes the file with arbitrary data in JSON format and displays its content in the console in an easy-to-read form: adds line breaks, left indents and spaces.

# Quickstart

```python
from pprint_json.py import load_data()
from pprint_json.py import pprint_json()
...
if __name__ = "main":
    file = 'filename.json'
    pprint_json(load_data(file))
```

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
{
    "menu": "",
    "commands": [
        {
            "title": "New",
            "action": "CreateDocument"
        },
        {
            "title": "Open",
            "action": "OpenDocument"
        },
        {
            "title": "Close",
            "action": "CloseDocument"
        }
    ]
}


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
