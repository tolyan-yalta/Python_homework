# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import sys
import datetime


def deposit(cash):
    """Зачисление средств на счет"""
    cash_up = int(input("Укажите вносимую сумму --> "))
    if cash_up % 50 == 0:
        cash +=cash_up
        cash = tax_collection(cash)
    else:
        deposit()
    return cash, cash_up


def cashout(cash):
    """Снятие средств со счета"""
    cash = tax_collection(cash)
    cash_out = int(input("Укажите снимаемую сумму --> "))
    if cash_out % 50 == 0 and cash_out < cash:
        cash -=cash_out
        cash = cash - (30 if cash * 0.015 < 30 else (600 if cash * 0.015 > 600 else cash * 0.015))
    else:
        cashout()
    return cash, cash_out


def tax_collection(cash):
    """Сбор налога с суммы больше 5_000_000"""
    if cash > 5_000_000:
        cash = cash - ((cash - 5_000_000) * 0.1)
    return cash


def start():
    # Средства на счету
    cash = 0
    # Счетчик количества операций
    count = 0
    # Список операций
    list_operations = []

    while True:
        print(f"На счету сумма {cash}")
        action = int(input("Введите операцию: 1 -пополнить, 2 - снять, 3 - вывести список операций, 4 - выйти --> "))
        
        match action:
            case 1:
                cash, cash_up = deposit(cash)
                list_operations.append(f"{datetime.datetime.now()} Зачислена сумма {cash_up}")
            case 2:
                cash, cash_out = cashout(cash)
                list_operations.append(f"{datetime.datetime.now()} Снята сумма {cash_out}")
            case 3:
                for i in list_operations:
                    print(i)
                continue
            case 4:
                print("Спасибо что воспользовались нашим банкоматом. Приходите ещё!")
                sys.exit()

        # Счетчик операций и начисление 3 %
        count += 1
        if count % 3 == 0:
            cash = cash * 1.03
            list_operations.append(f"{datetime.datetime.now()} Начислены проценты (3 %) {round(cash * 0.03, 2)}")
    

start()
