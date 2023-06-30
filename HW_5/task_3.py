# Создайте функцию генератор чисел Фибоначчи.


def fibonacci():
    """Функция генератор чисел Фибоначчи"""
    numbers = [0, 1]
    i = 0
    while True:
        if i == 0:
            yield numbers[i]
            i += 1
        elif i == 1:
            yield numbers[i]
            i += 1
            numbers.append(numbers[i - 1] + numbers[i - 2])
        else:
            yield numbers[i]
            i += 1
            numbers.append(numbers[i - 1] + numbers[i - 2])


# Количество элементов числовой последовательности (начиная с 0)
count = 11
for n in fibonacci():
    print(n)
    count -= 1
    if count == 0:
        break

# Или можно вывести в таком варианте
# obj = fibonacci()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
