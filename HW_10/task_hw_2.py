# Превратите функции в методы класса. Задачи должны решаться через 
# вызов методов экземпляра.

# > Задача 5 из семинара 8.
# > Напишите функцию, которая ищет json файлы в указанной директории 
# > и сохраняет их содержимое в виде одноименных pickle файлов.

import json
import pickle
from pathlib import Path

class Folder():

    def __init__(self, directory):
        self.directory = directory

    def from_json_to_pickle(self):
        files = [f for f in Path(self.directory).iterdir() if f.suffix == ".json"]
        for file in files:
            with (
                open(file, "r", encoding="utf-8") as f_j,
                open(f"{self.directory}\{file.stem}.pickle", "wb") as f_p    # stem Получить имя файла без расширения.
            ):
                data = json.load(f_j)
                pickle.dump(data, f_p)


example = Folder("HW_10")
example.from_json_to_pickle()
