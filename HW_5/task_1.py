# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def separator_string(str_):
    path, name_ext = str_.rsplit(sep=chr(92), maxsplit=1)
    return {*name_ext.rsplit(sep=".", maxsplit=1), path}


str_ = "G:\GeekBrains\Погружение_в_Python\Python_homework\README.md"
res = separator_string(str_) 
print(res)
