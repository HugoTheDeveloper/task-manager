import json
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent


def from_json(file_name):
    with open(APP_DIR / 'fixtures' / file_name) as file:
        return json.load(file)
