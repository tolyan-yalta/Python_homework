# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки 
# ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки. 
# *Выведите все успешные варианты расстановок

import random
from check import check_placement, SIZE, NUMBER_QUEENS


def random_placement():
    count = 4
    while count > 0:
        # кортеж с координатами, где [0] - горизонталь, [1] - вертикаль
        example = [(random.randint(1, SIZE), random.randint(1, SIZE)) for _ in range(NUMBER_QUEENS)]
        if len(set(example)) < NUMBER_QUEENS:
            continue
        if check_placement(*example):
            print(example)
            count -= 1


if __name__ == "__main__":
    random_placement()

    # [(7, 1), (1, 4), (3, 3), (5, 2), (2, 7), (6, 5), (8, 6), (4, 8)]
    # 
    # 
    # 
