# Доработаем задачи 3 и 4. 
# Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. 
# Класс имеет следующие методы: 
# * Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# * Метод входа в систему – требует указать имя и id пользователя. 
#   Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта. 
#   Если в списке его нет, то вызывается исключение доступа. 
#   Если пользователь присутствует в списке пользователей проекта, то пользователь, 
#   который входит получает его уровень доступа и становится администратором.
# * Метод добавление пользователя в список пользователей. 
#   Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

from class_my_exception import AccessError, LevelError, DeleteUserError
from class_user import User
import json

class Project:
    """Класс Project"""
    user_list = []
    FILE_PATH = "HW_13/example.json"
    ADMIN_LEVEL = 3

    def __init__(self):
        # Я сделал в конструкторе атрибут current_user, а не admin и для проверки прав админа
        # в методах сравниваю его level с константой ADMIN_LEVEL
        self.current_user = None
        Project.read_json()

    def __str__(self) -> str:
        return f"Current user: {self.current_user}, list users: {[user.__str__() for user in Project.user_list]}"

    @classmethod
    def read_json(cls):
        """Метод чтения пользователей из json файла."""
        with open(Project.FILE_PATH, 'r', encoding='utf-8') as f:
            dict_json = json.load(f)
        for level, value in dict_json.items():
            for id, name in value.items():
                cls.user_list.append(User(name, int(id), int(level)))

    @staticmethod
    def input_name():
        """Ввод имени состоящего только из букв и начинающегося с заглавной буквы."""
        while True:
            name = input("Введите имя пользователя: --> ")
            if name.isalpha() and name.istitle():
                return name
            print("Имя должно состоять только из букв и начинаться с заглавной буквы!")

    @staticmethod
    def input_id():
        """Ввод ID состоящего только из десятичных цифр."""
        while True:
            id = input("Введите ID: --> ")
            if id.isdecimal():
                return int(id)
            print("ID должен состоять только из десятичных цифр!") 

    @staticmethod
    def input_level():
        """Ввод уровня доступа."""
        while True:
            try:
                level = int(input("Введите уровень: --> "))
                if 1 <= level <= 7:
                    return level
                print("Уровень может быть от 1 до 7!")
            except ValueError:
                print("Уровень может быть только целым числом от 1 до 7!")

    def add_id(self):
        """Метод создает множество из ID пользователей и затем проверяет,
        есть ли новый ID в нем и если нет, то возвращает его."""
        set_id = set()
        for user in Project.user_list:
            set_id.add(user.user_id)
        while True:
            self.new_id = self.input_id()
            if self.new_id in set_id:
                print("Такой ID уже есть! Придумайте другой.")
                continue
            return self.new_id

    def logon(self):
        """Метод входа в систему. Запрашивает имя и ID, а затем создает временного пользователя temp_user.
        Проверяет есть ли такой в списке пользователей и если есть, то в self.current_user присваивает
        соответствующее значение из списка (т.е. из списка добавляется еще и уровень доступа).
        Иначе вызывается исключение AccessError."""
        name = self.input_name()
        id = self.input_id()
        temp_user = User(name, id)
        for value in self.user_list:
            if temp_user.__eq__(value) :
                self.current_user = value
                break
        else:
            raise AccessError(name, id)
        
    def save_user_list(self):
        """Метод записи списка пользователей в файл json"""
        with open(Project.FILE_PATH, 'w', encoding='utf-8') as f:
        # with open("task_5_2.json", 'w', encoding='utf-8') as f:
            dict_ = {}
            for user in Project.user_list:
                if dict_.setdefault(user.user_level) == None:
                    dict_[user.user_level] = {user.user_id: user.user_name}
                else:
                    temp = dict_.get(user.user_level)
                    temp[user.user_id] = user.user_name
            json.dump(dict_, f, indent=4)

    def add_user(self):
        """Метод добавления нового пользователя.
        Сначала проверяется достаточен ли уровень доступа текущего пользователя
        (если нет, то вызывается исключение LevelError), 
        затем запрашиваются данные нового пользователя, добавляется пользователь 
        и вызывается метод записи в файл json."""
        if self.current_user.user_level > Project.ADMIN_LEVEL:
            raise LevelError(self.current_user, Project.ADMIN_LEVEL)
        new_name = self.input_name()
        new_id = self.add_id()
        while True:
            new_level = self.input_level()
            # Уровень добавляемого пользователя не может быть меньше уровня текущего пользователя
            if new_level < self.current_user.user_level:
                print("Уровент добавляемого пользователя \
не может быть выше по правам доступа уровня текущего пользователя!")
            else:
                break
        Project.user_list.append(User(new_name, new_id, new_level))
        self.save_user_list()

    def del_user(self):
        """Метод удаления пользователя
        Сначала проверяется достаточен ли уровень доступа текущего пользователя
        (если нет, то вызывается исключение LevelError). 
        Затем запрашиваются данные удаляемого пользователя и содается временный пользователь,
        который ищется в списке пользователей. Если не находится, то вызывается исключение DeleteUserError, 
        а если находится, то удаляется и вызывается метод записи в файл json."""
        if self.current_user.user_level > Project.ADMIN_LEVEL:
            raise LevelError(self.current_user, Project.ADMIN_LEVEL)
        del_name = self.input_name()
        del_id = self.input_id()
        temp_user = User(del_name, del_id)
        for value in self.user_list:
            if temp_user.__eq__(value) :
                Project.user_list.remove(temp_user)
                break
        else:
            raise DeleteUserError(del_name, del_id)
        self.save_user_list()


if __name__ == "__main__":
    proj = Project()
    print(proj)
    proj.logon()
    print(proj)
    print("Добавляем пользователя.")
    proj.add_user()
    print(proj)
    print("Удаляем пользователя.")
    proj.del_user()
    print(proj)
