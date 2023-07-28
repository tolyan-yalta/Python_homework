# Задание №4
# Вспомните задачу из семинара 8 про сериализацию данных, 
# где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# * Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. 
# * Реализуйте магический метод проверки на равенство пользователей

class User:
    """Класс Пользователь"""

    def __init__(self, user_name, user_id, user_level=None):
        self.user_name = user_name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        """Метод сравнивает пользователей по имени и ID."""
        return self.user_name == other.user_name and self.user_id == other.user_id
    
    def __str__(self) -> str:
        return f"{self.user_name} {self.user_id} {self.user_level}"
    