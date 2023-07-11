# Напишите функцию, которая генерирует псевдоимена. 
# Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# Полученные имена сохраните в файл

from random import randint, choice


def generation_name(file_name: str, quantity: int):
    vowel_letter = "aeiouy"
    alphabet_letter = "abcdefghijklmnopqrstuvwxyz"
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(quantity):
            name = choice(alphabet_letter).upper()
            for __ in range(randint(3, 5)):
                name = name + choice(alphabet_letter)
            if len(set(name).intersection(set(vowel_letter))) == 0:
                name = name + choice((vowel_letter))
            f.write(f"{name}\n")


if __name__ == "__main__":
    generation_name("task_2.txt", 10)
