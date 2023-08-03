# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import os.path
from pathlib import Path
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename="homework.log",
                    encoding="utf-8",
                    level=logging.DEBUG)
logger = logging.getLogger()

Dates = namedtuple('Dates', ['name', 'type_obj', 'parent'])

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, default=os.getcwd())
args = parser.parse_args()


def recursive_folder_traversal(directory):
    """Функция, которая получает на вход директорию и рекурсивно обходит её и все 
    вложенные директории."""

    for dir_path, list_dir, list_file_names in os.walk(directory):
        # Первое значение кортежа возвращаемого os.walk это путь к текущему каталогу
        # получаем имя 
        dir_name = os.path.basename(dir_path)
        # Можно было бы через Path.is_dir() получить что это каталог, 
        # но и так знаем что это каталог
        type_obj = "dir"
        # получаем имя родительского каталога
        parent = os.path.basename(os.path.dirname(dir_path))
        # создаем именованный кортеж для каталога
        date_dir_log = Dates(dir_name, type_obj, parent)
        logger.info(f'{date_dir_log = }')
        if len(list_file_names) != 0:
            for file_name_str in list_file_names:
                file_path = os.path.join(dir_path, file_name_str)
                temp_obj = Path(file_path)
                if temp_obj.is_symlink():
                    file_name = temp_obj.stem
                    type_obj = "symlink"
                    parent = dir_name
                    date_file_log = Dates(file_name, type_obj, parent)
                    logger.info(f'{date_file_log = }')
                elif temp_obj.is_file():
                    file_name = temp_obj.stem
                    type_obj = temp_obj.suffix[1:]
                    if type_obj == "":
                        type_obj = "file without extension"
                    parent = dir_name
                    date_file_log = Dates(file_name, type_obj, parent)
                    logger.info(f'{date_file_log = }')


recursive_folder_traversal(args.directory)

# python homework.py -d "./Folder_with_examples/Лекции url"
# python homework.py -d "./Folder_with_examples"
# python homework.py
