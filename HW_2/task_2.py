# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import fractions


def input_fraction():
    """Функция для ввода дроби"""
    while True:
        str = input("Введите дробь в виде 'числитель/знаменатель'\n" \
                    "По определению:\n" \
                    "числитель - целое число\n" \
                    "знаменатель - натуральное число\n" \
                    "--> ")
        str_fraction = str.split(sep="/")
        # проверка числителя (numerator) на отрицательное целое число
        if str_fraction[0][:1] == "-":
            if str_fraction[0][1:].isdigit():
                numerator = int(str_fraction[0])
        # проверка числителя на целое число
        elif str_fraction[0].isdigit():
            numerator = int(str_fraction[0])
        # неправильный ввод
        else:
            print("Вы ввели не целое число в числитель!")
            continue
        # проверка знаменателя (denominator) на целое число
        if str_fraction[1].isdigit():
            # проверка знаменателя на 0
            if int(str_fraction[1]) == 0:
                print("Знаменатель не может быть = 0 !")
                continue
            else:
                denominator = int(str_fraction[1])
        # неправильный ввод        
        else:
            print("Вы ввели не натуральное число в знаменатель!")
            continue
        break
    # Создание переменной через модуль 'fraction' <class 'fractions.Fraction'>
    fraction = fractions.Fraction(int(str_fraction[0]), int(str_fraction[1]))
    print("-" * 25)
    return numerator, denominator, fraction


def summation_fractions(numerator_1, denominator_1, numerator_2, denominator_2):
    """Функция сложения дробей"""
    res_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    res_denominator = denominator_1 * denominator_2
    print("Сложение дробей (реализованная функция):\t"\
          f"{numerator_1}/{denominator_1} + {numerator_2}/{denominator_2}", end=" ")
    # сокращение дроби
    res_numerator, res_denominator = reduction_fractions(res_numerator, res_denominator)
    print(f"= {int(res_numerator)}/{int(res_denominator)}")
    

def multiplication_fractions(numerator_1, denominator_1, numerator_2, denominator_2):
    """Функция перемножения дробей"""
    res_numerator = numerator_1 * numerator_2
    res_denominator = denominator_1 * denominator_2
    print("Умножение дробей (реализованная функция):\t"\
          f"{numerator_1}/{denominator_1} * {numerator_2}/{denominator_2}", end=" ")
    # сокращение дроби
    res_numerator, res_denominator = reduction_fractions(res_numerator, res_denominator)
    print(f"= {int(res_numerator)}/{int(res_denominator)}")


def reduction_fractions(numerator, denominator):
    """сокращение дроби"""
    i = 9
    while i > 1:
        if numerator % i == 0 and denominator % i == 0:
            numerator /= i
            denominator /= i
            i = 9
            continue
        i -= 1
    return numerator, denominator



# Ввод первой дроби
print("Введите первую дробь:")
numerator_1, denominator_1, fraction_1 = input_fraction()
# Ввод второй дроби
print("Введите вторую дробь:")
numerator_2, denominator_2, fraction_2 = input_fraction()

# Сложение дробей
summation_fractions(numerator_1, denominator_1, numerator_2, denominator_2)
# Сложение дробей через 'fraction'
print(f"Сложение дробей (Модуль 'fraction'):\t\t{fraction_1} + {fraction_2} = {fraction_1 + fraction_2}\n")

# Умножение дробей
multiplication_fractions(numerator_1, denominator_1, numerator_2, denominator_2)
# Умножение дробей через 'fraction'
print(f"Умножение дробей (Модуль 'fraction'):\t\t{fraction_1} * {fraction_2} = {fraction_1 * fraction_2}")
