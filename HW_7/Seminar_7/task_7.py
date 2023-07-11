# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from pathlib import PurePath

def sorting_files(directory):
    list_ = os.listdir(directory)
    groups = {
                'video': ['avi', 'mkv'],
                'image': ['jpg', 'png', 'bmp'],
                'text': ['txt', 'rtf']
            }
    for file in list_:
        for group, list_ext in groups.items():
            ext = PurePath(file).suffix[1:]
            if ext in list_ext:
                if not os.path.isdir(f"{directory}\{group}"):
                    os.mkdir(f"{directory}\{group}")
                os.replace(f"{directory}/{file}", f"{directory}/{group}/{file}")


if __name__ == "__main__":
    sorting_files("Folder_with_examples")
