# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на 
# единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_not_int(value):
    '''Проверка введенного значения на не целое число'''
    try:
        int(value)
        return False
    except ValueError:
        return True


def input_number(LOWER_LIMIT, UPPER_LIMIT):
    '''Ввод целого числа в заданном диапазоне'''
    while True:
        number = input(F'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: --> ')
        if is_not_int(number):
            print("Вы ввели не целое число")
            continue
        number = int(number)
        if number < LOWER_LIMIT or number > UPPER_LIMIT:
            print("Вы ввели число вне указанного диапазона")
            continue
        else:
            break
    return number
    

def simple_number(number):
    '''Проверка простое ли число'''
    if number == 1 or number == 2 or number  == 3:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i**2 < number:
        if number % i == 0:
            return False
        i += 2 
    return True


LOWER_LIMIT = 1
UPPER_LIMIT = 100_000

value = input_number(LOWER_LIMIT, UPPER_LIMIT)
if simple_number(value):
    res = "Введенное число простое"
else:
    res = "Введенное число составное"
print(res)
