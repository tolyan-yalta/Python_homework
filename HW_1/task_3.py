# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 10
print(f"Угадайте число, у Вас {count} попыток")
while count > 0:
    value = int(input(f"Угадайте число, вводите --> "))
    if value == num:
        print(f"Вы угадали, загаданное число: {num}")
        break
    elif count == 1:
        count -= 1
        continue
    elif value < num:
        count -= 1
        print(f"Не угадали, загаданное число больше. Осталось {count} попыток")
    else:
        count -= 1
        print(f"Не угадали, загаданное число меньше. Осталось {count} попыток")
else:
    print("Не угадали. Попытки закончились.")
