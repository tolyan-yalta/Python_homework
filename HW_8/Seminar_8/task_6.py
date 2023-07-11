# Напишите функцию, которая преобразует pickle файл хранящий список словарей 
# в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def from_pickle_to_csv(file_pickle, file_csv):
    with (
        open(file_pickle, "rb") as f_load,
        open(file_csv, "w", newline='', encoding='utf-8') as f_write
    ):
        new_list = pickle.load(f_load)
        field_names = list(new_list[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=field_names, quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(new_list)


if __name__ == "__main__":
    from_pickle_to_csv("task_4.pickle", "task_6.csv")
