# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
import random
import string


def create_files_and_directory(directory, ext, min_length=6, max_length=30, min_bite=256, max_bite=4096, count=42):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    while count > 0:
        # Генерируется список букв длиной от min_length до max_length и объединяется в имя файла
        name = "".join([random.choice(string.ascii_letters) for __ in range(random.randint(min_length, max_length))])
        if not os.path.isfile(name):
            with open(f"{directory}\{name}.{ext}", "wb") as f:
                # Генерируется n (в заданном диапазоне) случайных байт
                data = random.randbytes(random.randint(min_bite, max_bite))
                f.write(data)
            count -= 1


def creating_different_files_and_folders(**kwargs):
    for key, item in kwargs.items():
        # print(key, item[0], item[1])
        create_files_and_directory(key, item[0], count=item[1])


if __name__ == "__main__":
    # create_files_and_directory("Files", "bin", count=5)
    creating_different_files_and_folders(Files_with_bin=("bin", 5), Files_with_pickle=("pickle", 3))
