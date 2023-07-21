# Превратите функции в методы класса. Задачи должны решаться через 
# вызов методов экземпляра.

# > Задача 2 из семинара 7.
# Напишите функцию, которая генерирует псевдоимена. 
# Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# Полученные имена сохраните в файл

from random import randint, choice

class FileName():

    def __init__(self, file_name, quantity):
        self.file_name = file_name
        self.quantity = quantity

    def generation_name(self):
        vowel_letter = "aeiouy"
        alphabet_letter = "abcdefghijklmnopqrstuvwxyz"
        with open(self.file_name, "a", encoding="utf-8") as f:
            for _ in range(self.quantity):
                name = choice(alphabet_letter).upper()
                for __ in range(randint(3, 5)):
                    name = name + choice(alphabet_letter)
                if len(set(name).intersection(set(vowel_letter))) == 0:
                    name = name + choice((vowel_letter))
                f.write(f"{name}\n")


example = FileName("HW_10/task_hw_3.txt", 10)
example.generation_name()
