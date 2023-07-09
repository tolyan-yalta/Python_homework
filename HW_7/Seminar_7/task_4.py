# Создайте функцию, которая создаёт файлы с указанным расширением. 
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

import os
import random
import string


def create_files(ext, min_length=6, max_length=30, min_bite=256, max_bite=4096, count=42):
    directory = "Files"
    if not os.path.isdir(directory):
        os.mkdir(directory)
    for _ in range(count):
        # Генерируется список букв длиной от min_length до max_length и объединяется в имя файла
        name = "".join([random.choice(string.ascii_letters) for __ in range(random.randint(min_length, max_length))])
        with open(f"{directory}\{name}.{ext}", "wb") as f:
            # Генерируется n (в заданном диапазоне) случайных байт
            data = random.randbytes(random.randint(min_bite, max_bite))
            f.write(data)


if __name__ == "__main__":
    create_files("bin", count=5)
