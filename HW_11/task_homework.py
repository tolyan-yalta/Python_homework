# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц

class Matrix:
    """Класс Матрица"""

    def __init__(self, list_of_lists):
        """Конструктор матрицы."""
        self.matrix = list_of_lists
        self.size = len(list_of_lists)

    def __str__(self) -> str:
        """Выводит матрицу в строчном виде."""
        return '\n'.join([''.join([f'{i}\t' for i in row]) for row in self.matrix])
    
    def __repr__(self):
        return f"Matrix({self.matrix})"
         
    def __eq__(self, other) -> bool:
        """Сравнение матриц по размеру."""
        return self.size == other.size
    # !!!Но это не значит, что матрацы будут равны, так что тут у вас ошибка.
    
    def __add__(self, other):
        """Сложение матриц. Складывает соответствующие элементы двух матриц
        и заносит результат в итоговую матрицу"""
        res_m = [[] for _ in range(self.size)]
        for i in range(self.size):
            res_m[i] = [None for __ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                res_m[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res_m)
    
    def __mul__(self, other):
        """Произведение матриц. Для того, чтобы найти произведение матриц нужно 
        строки первой матрицы умножить на столбцы второй матрицы."""
        res_m = [[] for _ in range(self.size)]
        for i in range(self.size):
            res_m[i] = [None for __ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                i = 0
                temp = 0
                while i < self.size:
                    temp += self.matrix[row][i] * other.matrix[i][col]
                    i += 1
                res_m[row][col] = temp
        return Matrix(res_m)


list_of_lists_1 = [[2, 1], [-3, 4]]
m_1 = Matrix(list_of_lists_1)
print(m_1)
print("*" * 25)
list_of_lists_2 = [[1, -3], [2, 0]]
m_2 = Matrix(list_of_lists_2)
print(m_2)

print(f"Результат сравнения размеров матриц: {m_1 == m_2}")

m_3 = m_1 + m_2
print("Выводим на печать результат сложения матриц")
print(m_3)

m_4 = m_1 * m_2
print("Выводим на печать результат перемножения матриц")
print(m_4)
# Если взять пример с https://математика24.рф/proizvedenie-matric.html
# |2    1| X |1   -3| = |4  -6|
# |-3   4|   |2    0|   |5   9|
# то ответ сходится
print(repr(m_4))
