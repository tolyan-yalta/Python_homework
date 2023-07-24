# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц

class Matrix:
    """Класс Матрица"""

    def __init__(self, size: int):
        """Конструктор матрицы. Создает 'size' строк, каждая из которых
        состоит из 'size' элементов и заполняет их 'None'."""
        self.size = size
        self.matrix = [None for _ in range(self.size)]
        for i in range(self.size):
            self.matrix[i] = [None for __ in range(self.size)]
            
    def fill_matrix(self):
        """Заполнение матрицы."""
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = int(input(f"Введите {i}{j} элемент матрицы: --> "))

    def __str__(self) -> str:
        """Выводит матрицу в строчном виде."""
        return '\n'.join([''.join([f'{i}\t' for i in row]) for row in self.matrix])
    
    def __repr__(self):
        return f"Matrix({self.size})"
         
    def __eq__(self, other) -> bool:
        """Сравнение матриц по размеру."""
        return self.size == other.size
    
    def __add__(self, other):
        """Сложение матриц. Складывает соответствующие элементы двух матриц
        и заносит результат в итоговую матрицу"""
        res_m = Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                res_m.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return res_m
    
    def __mul__(self, other):
        """Произведение матриц. Для того, чтобы найти произведение матриц нужно 
        строки первой матрицы умножить на столбцы второй матрицы."""
        res_m = Matrix(self.size)
        for row in range(self.size):
            for col in range(self.size):
                i = 0
                temp = 0
                while i < self.size:
                    temp += self.matrix[row][i] * other.matrix[i][col]
                    i += 1
                res_m.matrix[row][col] = temp
        return res_m


print("Создаем и заполняем первую матрицу")
m_1 = Matrix(2)
m_1.fill_matrix()
print("*" * 25)
print("Создаем и заполняем вторую матрицу")
m_2 = Matrix(2)
m_2.fill_matrix()
print("Выводим на печать первую матрицу")
print(m_1)
print("Выводим на печать вторую матрицу")
print(m_2)

print(f"Результат сравнения размеров матриц: {m_1 == m_2}")

m_3 = m_1 + m_2
print("Выводим на печать результат сложения матриц")
print(m_3)
# Если взять пример с https://математика24.рф/proizvedenie-matric.html
# |2    1| X |1   -3| = |4  -6|
# |-3   4|   |2    0|   |5   9|
# то ответ сходится
m_4 = m_1 * m_2
print("Выводим на печать результат перемножения матриц")
print(m_4)

print(repr(m_4))
