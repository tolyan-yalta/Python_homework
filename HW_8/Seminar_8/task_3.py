# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv


def from_json_to_csv():
    with (
        open("task_2.json", "r", encoding="utf-8") as f1,
        open("task_3.csv", "w", encoding="utf-8", newline='') as f2 # без newline='' записывает через строку
    ):
        dict_ = json.load(f1)
        list_ = []
        for level, val in dict_.items():
            for id_, name in val.items():
                list_.append({
                    "id": id_,
                    "name": name,
                    "level": level
                })
        csv_wr = csv.DictWriter(f2, fieldnames=list_[0].keys())
        csv_wr.writeheader()
        csv_wr.writerows(list_)


if __name__ == "__main__":
    from_json_to_csv()
