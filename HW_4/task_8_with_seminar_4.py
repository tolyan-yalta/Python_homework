# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
# (кроме переменной из одной буквы s) на None. Значения не удаляются, 
# а помещаются в одноимённые переменные без s на конце.


def change_content():
    """Функция изменения и создания переменных в глобальной области видимости"""
    g_n = globals()
    for key in list(g_n.keys()):
        if len(key) > 1 and key[-1:] == "s":
            g_n[key[:-1]], g_n[key] = g_n[key], None
    

datas = [42, -73, 12, 85, -15, 2]
s = "Hello world"
names = ("no_name", "other_name", "new_name")
sx= 42

print("До вызова функции:")
print(f"datas = {datas}")
print(f"s = {s}")
print(f"names = {names}")
print(f"sx = {sx}")
print("-" * 25)
            
change_content()

print("После вызова функции:")
print(f"datas = {datas}")
print(f"s = {s}")
print(f"names = {names}")
print(f"sx = {sx}")
print("-" * 25)

print("Новые переменные:")
print(f"data = {data}")
print(f"name = {name}")
