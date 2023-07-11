# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор 
# и уровень доступа (от 1 до 7). 
# После каждого ввода добавляйте новую информацию в JSON файл. 
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. 
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json


def read_user():

    while True:
        name = input("Введите имя --> ")
        id = input("Введите id --> ")
        level = input("Введите уровень доступа --> ")
        
        try:
            with open('task_2.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        if level not in data.keys():
            data[level] = {}
        data[level][id] = name
        with open("task_2.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    read_user()
