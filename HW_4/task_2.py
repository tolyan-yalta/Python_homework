# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


list_ = [4, True, 6.8, "Hi"]
str_ = "hello"
int_ = 8
dict_ = {"key1": 1, "key2": 2}


def given_function(*, arg):
    dict_res = {}
    temp = globals()
    for key in temp:
        if temp[key] == arg:
            dict_res[str(arg)] = key
    if len(dict_res) == 0:
        dict_res[str(arg)] = None
    return dict_res


print(given_function(arg=list_))
print(given_function(arg=str_))
print(given_function(arg=int_))
print(given_function(arg=dict_))
print(given_function(arg=5))
