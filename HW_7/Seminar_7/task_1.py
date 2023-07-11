# Напишите функцию, которая заполняет файл 
# (добавляет в конец) случайными парами чисел. 
# Первое число int, второе - float разделены вертикальной чертой. 
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform


def fill_file(file_name: str, quantity: int):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(quantity):
            f.write(f"{randint(MIN_NUMBER, MAX_NUMBER)} | {uniform(MIN_NUMBER, MAX_NUMBER)}\n")


MIN_NUMBER = -1000
MAX_NUMBER = 1000

if __name__ == "__main__":
    fill_file("task_1.txt", 10)
