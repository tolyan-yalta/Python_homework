# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

from random import uniform
import os
import csv
import json

# Количество строк генерируемое в файле csv
NUMBER = 100


def number_rows(num):
    def deco(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(num)]
        return wrapper
    return deco


@number_rows(NUMBER)
def three_number_generator():
    """Генерация csv файла с тремя случайными числами в каждой строке."""
    rand_min = -100
    rand_max = 100
    with open("HW_9/generated_numbers.csv", "a", encoding="utf-8", newline='') as f:
        numbers = [round(uniform(rand_min, rand_max), 2) for _ in range(3)]
        csv_write = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(numbers)


def deco_finding_roots(func):
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""
    def wrapper(*args, **kwargs):
        with open("HW_9/generated_numbers.csv", "r", encoding="utf-8", newline='') as f_csv:
            csv_file = csv.reader(f_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)

            for args in csv_file:
                res = func(*args, **kwargs)
        return res
    
    return wrapper
        


def save_json(func):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
    if os.path.exists("HW_9/results.json"):
        with open("HW_9/results.json", "r", encoding="utf-8") as f:
            list_res = json.load(f)
    else:
        list_res = []
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        a, b, c = args
        res = {
            "a": a,
            "b": b,
            "c": c}
        if func_res == None:
            res["x"] = None
        # Если дискриминант = 0 и в решении один корень
        elif type(func_res) == float:
            res["x"] = func_res
        else:
            res["x1"] = func_res[0]
            res["x2"] = func_res[1]
        list_res.append(res)

        with open("HW_9/results.json", "w", encoding="utf-8") as f_json:
            json.dump(list_res, f_json, indent=4)

        return func_res   
    return wrapper



@deco_finding_roots
@save_json
def finding_roots(*args):
    """Нахождение корней квадратного уравнения"""
    a, b, c = args
    discr =  b ** 2 - 4 * a * c
    if discr < 0:
        return None
    elif discr == 0:
        return round(-b / (2 * a), 2)
    else:
        return round((-b + discr ** 0.5) / (2 * a), 2), round((-b - discr ** 0.5) / (2 * a), 2)


if __name__ == "__main__":
    three_number_generator()
    print(finding_roots())
