# Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните 
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# При достижении конца более короткого файла, 
# возвращайтесь в его начало.


def task_3(file_name_1: str, file_name_2: str, file_name_res: str):
    with open(file_name_1, "r", encoding="utf-8") as f1, \
        open(file_name_2, "r", encoding="utf-8") as f2, \
        open(file_name_res, "+a", encoding="utf-8") as f3:
        #
        #
        file_end_1 = False
        file_end_2 = False
        while True:
            temp_f1 = f1.readline()
            if temp_f1 == "":
                file_end_1 = True
                f1.seek(0, 0)
                continue
            temp_f2 = f2.readline()
            if temp_f2 == "":
                file_end_2 = True
                f2.seek(0, 0)
                continue
            if file_end_1 and file_end_2:
                break

            num = int(temp_f1.split("|")[0].strip()) * float(temp_f1.split("|")[1].strip())
            if num < 0:
                f3.write(f"{temp_f2.strip().lower()}\t{abs(num)}\n")
            else:
                f3.write(f"{temp_f2.strip().upper()}\t{round(num, 0)}\n")


if __name__ == "__main__":
    task_3("task_1.txt", "task_2.txt", "task_3.txt")
