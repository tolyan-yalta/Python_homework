# Напишите функцию, которая ищет json файлы в указанной директории 
# и сохраняет их содержимое в виде одноименных pickle файлов.

import json
import pickle
from pathlib import Path

def from_json_to_pickle(directory):
    files = [f for f in Path(directory).iterdir() if f.suffix == ".json"]
    for file in files:
        with (
            open(file, "r", encoding="utf-8") as f_j,
            open(f"{file.stem}.pickle", "wb") as f_p    # stem Получить имя файла без расширения.
        ):
            data = json.load(f_j)
            pickle.dump(data, f_p)


if __name__ == "__main__":
    from_json_to_pickle(Path().cwd())
        



