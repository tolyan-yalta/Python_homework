# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, 
#   у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
#   на любое большее количество друзей.

group = {
    "Петя": ("палатка", "спальник", "фонарик", "газовая горелка", "термос", "посуда", "продукты", "вода"),
    "Иван": ("тент", "спальник", "дрова", "спички", "топор", "посуда", "продукты", "вода", "нож"),
    "Вася": ("надувная лодка", "спальник", "удочка", "динамит", "спички", "фонарик", "посуда", "продукты", "вода")
}

# Создаем (извлекаем) список друзей
list_friends = list(group.keys())

# Создаем словарь Ключ - имя : Значение - множество вещей
dict_set = {}
for i in list_friends:
    dict_set[str(i)] = set(group.get(i))


def identical_object_in_sets(dict_set, list_friends):
    """Нахождение пересечения множеств в словаре"""
    # Создаем переменную с вещами (множеством) первого друга
    friend_1_set = dict_set.get(list_friends[0])
    # и находим пересечение множеств, т. е. одинаковые для всех вещи
    identical_object = friend_1_set.intersection(*[dict_set.get(i) for i in list_friends])
    return identical_object


identical_object = identical_object_in_sets(dict_set,  list_friends)
print(f"Все друзья взяли: {identical_object}")
print("-" * 25)


for i in list_friends:
    temp_list_friends = list_friends[:]
    # Во временную переменную заносим вещи (множество) текущего друга
    temp_friend = dict_set.get(i)
    # Из временного списка друзей удаляем текущего друга
    temp_list_friends.remove(i)
    # Получаем уникальные вещи текущего друга
    different_object = temp_friend.difference(*[dict_set.get(i) for i in temp_list_friends])
    print(f"Только {i} взял: {different_object}")
print("-" * 25)

for i in list_friends:
    temp_list_friends = list_friends[:]
    # Во временную переменную заносим вещи (множество) текущего друга
    temp_friend = dict_set.get(i)
    # Из временного списка друзей удаляем текущего друга
    temp_list_friends.remove(i)
    # Делаем временную копию словаря
    temp_dict_set = dict_set.copy()
    # Из словаря множеств удаляем текущего друга
    del temp_dict_set[i]
    # Получаем общие вещи всех друзей кроме текущего
    temp_identical_object = identical_object_in_sets(temp_dict_set, temp_list_friends)
    # Получаем уникальные вещи друзей без текущего
    temp_different_object = temp_identical_object.difference(temp_friend)
    if len(temp_different_object) != 0:
        print(f"У всех есть: {temp_different_object} кроме {i}")
