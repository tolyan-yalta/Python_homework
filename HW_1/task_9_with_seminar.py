# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def table_band(min_value, max_value):
    for i in range(2, 11):
        for j in range(min_value, max_value):
            print(f"{j} X {i}{'' if i == 10 else ' '}={('  ' if j * i < 10 else ' ')}{j * i}\t", end='')
        print()
    print()
    

print(' ' * 20 + 'ТАБЛИЦА УМНОЖЕНИЯ')
table_band(2, 6)
table_band(6, 10)
