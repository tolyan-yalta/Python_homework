# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


my_list = [2, 4, 8, True, "qwe", 2, 9, "qwe", False, 1, "rty", 7, 2, True]
temp = []
for item in my_list:
    if my_list.count(item) > 1:
        temp.append(item)

res_list = list(set(temp))
print(res_list)
