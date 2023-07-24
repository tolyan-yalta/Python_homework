# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyStr(str):
    """К классу 'str' добавляем имя и время создания."""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.create_time = time.time()
        return instance
    
    def __str__(self) -> str:
        return str({"value": self} | self.__dict__)

    # def __repr__(self):
    #     return f'MyStr({self})'


str_1 = MyStr(10, "Vadim")
print(str_1)
# print(str_1.__repr__())
