# Задание №3
# * Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass

class LevelError(MyException):
    """Класс исключения: Ошибка уровня доступа!"""
    def __init__(self, user, admin_level):
        self.user = user
        self.admin_level = admin_level

    def __str__(self) -> str:
        return f"Ошибка уровня доступа! Уровень доступа текущего пользователя = {self.user.user_level}, \
а для добавления или удаления пользователей он должен быть <= {self.admin_level}."

class AccessError(MyException):
    """Класс исключения: Ошибка доступа!"""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Ошибка доступа! Или имя = {self.name} или ID = {self.id} отсутствуют в списке пользователей."

class DeleteUserError(MyException):
    """Класс исключения: Ошибка удаления пользователя!"""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Ошибка удаления пользователя! Пользователь с именем = {self.name} и \
ID = {self.id} отсутствует в списке пользователей."
