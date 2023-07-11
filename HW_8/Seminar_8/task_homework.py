# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

__all__ = ["recursive_folder_traversal"]

import os
import json
import csv
import pickle


def get_directory_size(directory):
    """Вычисление размера папки с рекурсивным обходом вложенных папок"""
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # Если встретился не каталог, а файл, то вернётся его размер
        return os.path.getsize(directory)
    except PermissionError:
        # Если папка не открывается, вернётся 0
        return 0
    return total


def recursive_folder_traversal(directory):
    """Функция, которая получает на вход директорию и рекурсивно обходит её и все 
    вложенные директории. Результаты обхода сохраняются в файлы json, csv и pickle."""
    # В список помещаем результат os.walk
    list_folders = []
    for dir_path, dir_name, file_name in os.walk(directory):
        list_folders.append([dir_path, dir_name, file_name])
    # Создаем словарь перебирая вышеуказанный список
    list_dict = []
    for folder in list_folders:
        for file in folder[2]:
                parent = os.path.basename(folder[0])
                size = os.stat(f"{folder[0]}\\{file}").st_size
                list_dict.append({
                    "obj": file,
                    "parent": parent,
                    "obj_type": "file",
                    "size": size
                })
        parent = os.path.basename(os.path.dirname(folder[0]))
        list_dict.append({
                    "obj": os.path.basename(folder[0]),
                    "parent": parent,
                    "obj_type": "dir",
                    "size": get_directory_size(folder[0])
                })

    # И записываем словарь в файлы
    with (
        open("task_hw.json", "w", encoding="utf-8") as f_j,
        open("task_hw.csv", "w", encoding="utf-8", newline='') as f_c,
        open("task_hw.pickle", "wb") as f_p
    ):
        json.dump(list_dict, f_j, indent=4)

        csv_write = csv.DictWriter(f_c, fieldnames=["obj", "parent", "obj_type", "size"], quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(list_dict)
        pickle.dump(list_dict, f_p)
            

if __name__ == "__main__":
    directory = os.getcwd()
    recursive_folder_traversal(directory)
