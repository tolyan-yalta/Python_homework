# Создайте класс Архив, который хранит пару свойств. Например, число и строку. 
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются 
# в пару списков-архивов list-архивы также являются свойствами экземпляра

class Archive:
    """Реализация паттерна Singleton"""

    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive = []
        else:
            cls._instance.archive.append([cls._instance.number, cls._instance.string])
        return cls._instance
    
    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self) -> str:
        return f"{self.number}, {self.string}, {self.archive}"

    def __repr__(self) -> str:
        return f"Archive({self.number}, {self.string})"


example_1 = Archive(1, "one")
print(example_1)
example_2 = Archive(2, "two")
print(example_2)
example_3 = Archive(3, "three")
print(example_3)
print(repr(example_3))
