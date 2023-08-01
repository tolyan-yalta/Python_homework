# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень). 
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
import json
import os
from project import Project
from user import User

@pytest.fixture
def get_file(tmpdir_factory):
    """Фикстура создающая временную папку и json файл со словарем.
    Файл создается для каждого теста, а затем удаляется."""
    users = {"1": {"123": "Ivan"},
            "2": {"236": "Gleb"},
            "7": {"741": "Karl"}}
    file_name = tmpdir_factory.mktemp("data").join("test_file.json")
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4)
    yield file_name
    os.remove(file_name)


def test_type_project(monkeypatch, get_file):
    """Тест для проверки типа объекта."""
    monkeypatch.setattr(Project, "FILE_PATH", get_file)
    proj = Project()
    assert type(proj) == Project, "TypeError!"


def test_project(monkeypatch, get_file):
    """Тест заменяет путь к файлу из константы на путь к файлу из фикстуры,
    очищает список пользователей, создает объект класса Project и
    сравнивает его с эталонным списком."""
    monkeypatch.setattr(Project, "FILE_PATH", get_file)
    monkeypatch.setattr(Project, "user_list", [])
    Project()
    assert [user.__str__() for user in Project.user_list] == ['Ivan 123 1', 'Gleb 236 2', 'Karl 741 7'], "Ошибка!"


def test_logon(monkeypatch, get_file):
    """Тест метода входа в систему, запрашивающий имя и ID."""
    monkeypatch.setattr(Project, "FILE_PATH", get_file)
    monkeypatch.setattr(Project, "user_list", [])
    proj = Project()
    responses = iter(['Gleb', "236"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    proj.logon()
    assert proj.current_user == User("Gleb", 236)


def test_add_user(monkeypatch, get_file):
    """Тест метода добавления пользователя."""
    monkeypatch.setattr(Project, "FILE_PATH", get_file)
    monkeypatch.setattr(Project, "user_list", [])
    proj = Project()
    responses = iter(['Gleb', "236"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    proj.logon()
    responses = iter(['Denis', "528", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    proj.add_user()
    assert [user.__str__() for user in Project.user_list] == \
            ['Ivan 123 1', 'Gleb 236 2', 'Karl 741 7', 'Denis 528 5'], "Ошибка!"
    

def test_del_user(monkeypatch, get_file):
    """Тест метода удаления пользователя."""
    monkeypatch.setattr(Project, "FILE_PATH", get_file)
    monkeypatch.setattr(Project, "user_list", [])
    proj = Project()
    responses = iter(['Gleb', "236"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    proj.logon()
    responses = iter(['Karl', '741'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    proj.del_user()
    assert [user.__str__() for user in Project.user_list] == ['Ivan 123 1', 'Gleb 236 2'], "Ошибка!"


if __name__ == '__main__':
    pytest.main(["-vv"])

# python -m pytest task_6.py -vv
