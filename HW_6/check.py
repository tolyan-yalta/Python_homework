# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

SIZE = 8
NUMBER_QUEENS = 8

def check_placement(*args):

    list_f = [*args]
    set_f = {*args}

    for i in range(1, NUMBER_QUEENS):
        # Получаем временный список без текущего элемента (ферзя)
        temp_list = list_f.copy()
        temp_list.remove(list_f[i])
        # Проверка совпадений по горизонтали
        for j in temp_list:
            if j[0] == list_f[i][0]:
                # print("совпадений по горизонтали")
                return False
        # Проверка совпадений по вертикали
        for j in temp_list:
            if j[1] == list_f[i][1]:
                # print("совпадений по вертикали")
                return False
        # Получаем временное множество без текущего элемента (ферзя)
        temp_set = set_f.copy()
        temp_set.remove(list_f[i])
        # Проверка вниз (вправо-лево) по диагонали
        k = 1
        for j in range(list_f[i][0] + 1, SIZE + 1):
            temp_doun_r = (j, list_f[i][1] + k)
            temp_doun_l = (j, list_f[i][1] - k)
            k += 1
            if temp_doun_r in temp_set or temp_doun_l in temp_set:
                # print("вниз (вправо-лево) по диагонали")
                # print(temp_doun_r, temp_doun_l)
                return False
        # Проверка вверх (вправо-лево) по диагонали
        k = 1
        for j in range(list_f[i][0] - 1, 0, -1):
            temp_up_r = (j, list_f[i][1] + k)
            temp_up_l = (j, list_f[i][1] - k)
            k += 1
            if temp_up_r in temp_set or temp_up_l in temp_set:
                # print("вверх (вправо-лево) по диагонали")
                # print(temp_up_r, temp_up_l)
                return False
    return True


if __name__ == "__main__":
    # кортеж с координатами, где [0] - горизонталь, [1] - вертикаль
    example = [(1, 4), (2, 1), (3, 5), (4, 8), (5, 6), (6, 3), (7, 7), (8, 2)]
    print(check_placement(*example))
