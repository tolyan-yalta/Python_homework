# Задание №5
# * Дорабатываем класс прямоугольник из прошлого семинара.
# * Добавьте возможность сложения и вычитания.
# * При этом должен создаваться новый экземпляр прямоугольника.
# * Складываем и вычитаем периметры, а не длинну и ширину.
# * При вычитании не допускайте отрицательных значений.


class Rectangle():
    """Rectangle - прямоугольник"""
    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width is None:
            self.width =length

    def perimetr(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def __add__(self, other):
        new_p = self.perimetr() + other.perimetr()
        new_length = self.length + other.length
        new_width = new_p / 2 - new_length
        return Rectangle(new_length, new_width)
    
    def __eq__(self, other) -> bool:
        """Сравнение по площади."""
        return self.area() == other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()
    
    def __str__(self) -> str:
        return f"Прямоугольник с длиной: {self.length} и шириной: {self.width}" \
            if self.length != self.width else f"Квадрат с сторонаим: {self.length}"
    
    def __repr__(self) -> str:
        return f"Rectangle({self.length}, {self.width})"


# r_1 = Rectangle(4, 8)   # p = 4*2 + 8*2 = 24
# r_2 = Rectangle(6, 5)   # p = 6*2 + 5*2 = 22
# r_3 = r_1 + r_2         # p = 46 n_l = 10 n_w = 13
# print(f"{r_1.__dict__} + {r_2.__dict__} = {r_3.__dict__}")
r_1 = Rectangle(3, 3)
r_2 = Rectangle(9, 1)
print(r_1.area())
print(r_2.area())
print(r_1 == r_2)

print(r_2)
print(repr(r_2))
