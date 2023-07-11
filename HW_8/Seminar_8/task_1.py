# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def create_json_file():
    with (
        open("task_1.txt", "r", encoding="utf-8") as f1,
        open("task_1.json", "w", encoding="utf-8") as f2
    ):
        data = f1.read().split("\n")
        dict_ = {}
        for i in data:
            if i == "":
                break
            key = i.split("\t")[0].upper()
            item = i.split("\t")[1]
            dict_[key] = item
        json.dump(dict_, f2, indent=4)


if __name__ == "__main__":
    create_json_file()
