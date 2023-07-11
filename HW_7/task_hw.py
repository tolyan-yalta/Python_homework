# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
#    При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
#    Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os
import pathlib


def rename_files(directory, new_file_name, new_ext_file, original_ext_files):
    list_files = os.listdir(path=directory)
    number = 1
    for file in list_files:
        if pathlib.PurePath(file).suffix == original_ext_files:
            os.rename(f"{directory}\{file}", f"{directory}\{pathlib.PurePath(file).stem}_{new_file_name}_{number}{new_ext_file}")
            number += 1


if __name__ == "__main__":
    directory = "HW_7\Task_HW"
    new_file_name = "newname" 
    new_ext_file = ".zip"
    original_ext_files = ".rtf"
    rename_files(directory, new_file_name, new_ext_file, original_ext_files)
