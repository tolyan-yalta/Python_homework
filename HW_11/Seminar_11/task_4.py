# Доработаем класс Архив из задачи 2. 
# Добавьте методы представления экземпляра для программиста и для пользователя.

def __str__(self) -> str:
    return f"{self.number}, {self.string}, {self.archive}"

def __repr__(self) -> str:
    return f"Archive({self.number}, {self.string})"

# Полностью см. в коде задачи № 2
