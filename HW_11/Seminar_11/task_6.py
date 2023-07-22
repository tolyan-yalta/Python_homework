# Задание №6
# * Доработайте прошлую задачу.
# * Добавьте сравнение прямоугольников по площади
# * Должны работать все шесть операций сравнения

def __eq__(self, other) -> bool:
    return self.area() == other.area()

def __ge__(self, other):
    return self.area() >= other.area()

def __gt__(self, other):
    return self.area() > other.area()

# Полностью см. в коде задачи № 5
