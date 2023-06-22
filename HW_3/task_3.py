# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import itertools

while True:
    max_weight = input("Ваедите максимальный вес рюкзака --> ")
    if max_weight.replace(".", "").isdecimal():
        max_weight = float(max_weight)
        break
    else:
        print("Вы ввели неправильное значение!")

staff = {
    'палатка': 5,
    'спальник': 2,
    'еда': 10,
    'вода': 10,
    'дрова': 20,
    'посуда': 5,
    'нож': 0.2,
    'спички': 0.02,
    'топор': 2,
    'фонарик': 0.5
}

quantity = len(staff)
while quantity > 0:
    print("\033[1m\033[33m\033[40m{}\033[0m".format(f"Количество вещей в рюкзаке = {quantity}"))
    spam = itertools.combinations(staff, quantity)
    for item in spam:
        weight = sum([staff.get(i) for i in item])
        if weight < max_weight:
            print(f"{item} общий вес = {weight:.2f} кг")
    quantity -= 1


