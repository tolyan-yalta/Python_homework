# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.


def input_number():
    """Функция для ввода целого числа"""
    while True:
        number = input("Введите целое число --> ")
        # проверка на отрицательное целое число
        if number[:1] == "-":
            if number[1:].isdigit():
                return int(number)
        # проверка на целое число
        elif number.isdigit():
            return int(number)
        # неправильный ввод
        else:
            print("Вы ввели не целое число!")


def convert_to_hex(number):
    """Преобразование в шестнадцатеричную систему счисления"""
    list = []
    prefix = ""
    if number == 0:
        return "0x0"
    elif number > 0:
        prefix = "0x"
    else:
        prefix = "-0x"
        number = abs(number)
    while number > 0:
        digit = str(number % BASIS)
        number = number // BASIS
        match digit:
            case "10":
                digit = "a"
            case "11":
                digit = "b"
            case "12":
                digit = "c"
            case "13":
                digit = "d"
            case "14":
                digit = "e"
            case "15":
                digit = "f"
        list.insert(0, digit)
    result = prefix + "".join(list)
    return result


def results_comparing(result_1, result_2):
    """Сравнение полученных результатов"""
    if result_1 == result_2:
        print("Все хорошо, результаты совпадают!")
    else:
        print("Что-то пошло не так! Результаты не совпадают!")


# основание шестнадцатеричной системы счисления
BASIS = 16

number = input_number()
result_hex = hex(number)
print(f"Результат преобразования через функцию 'hex' = {result_hex}")
result_def = convert_to_hex(number)
print(f"Результат преобразования через реализованную функцию = {result_def}")
results_comparing(result_hex, result_def)
