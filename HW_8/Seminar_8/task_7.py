# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle
import csv


def from_csv_to_pickle(file):
    with open(file, "r", newline="", encoding="utf-8") as f:
        csv_file = csv.reader(f, quoting=csv.QUOTE_ALL)
        list_ = []
        for i, (id_, name, level, hash_) in enumerate(csv_file):
            if i:
                list_.append({
                    "id": id_,
                    "name": name,
                    "level": level,
                    "hash": hash_
                })
        # print(list_)
        print(pickle.dumps(list_))
        

if __name__ == "__main__":
    from_csv_to_pickle("task_6.csv")
