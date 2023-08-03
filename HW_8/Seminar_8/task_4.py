# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv

def from_csv_to_json(file_csv, file_json):
    with (
        open (file_csv, "r", encoding="utf-8", newline="") as f1,
        open (file_json, "w", encoding="utf-8") as f2
    ):
        text_csv = csv.reader(f1)
        list_ = []
        for i, (id_, name, level) in enumerate(text_csv):
            if i:
                list_.append({
                    "id": id_.zfill(10),    # дополнит строку нулями
                    "name": name.capitalize(),  # первая буква в строке заглавная
                    "level": level,
                    "hash": hash(id_ + name)
                })
        json.dump(list_, f2, indent=4)


if __name__ == "__main__":
    from_csv_to_json("task_3.csv", "task_4.json")

# res.append(dict(zip(headers, [access, id_, name, name_hash])))
