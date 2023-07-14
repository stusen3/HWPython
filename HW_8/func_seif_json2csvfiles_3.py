#  Сохранить json файл в формате CSV

import os, csv, json
from pathlib import Path


def get_json2csvfiles(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                 json_file = json.load(js)

    rows = []
    for level, value in json_file.items():
        for id, name in value.items():
             rows.append({'level': level, 'user_id': id, 'name': name})

    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', ' user_id', ' name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    get_json2csvfiles(Path('./names.json'))