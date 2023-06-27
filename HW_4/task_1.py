# Напишите функцию для транспонирования матрицы.


def print_matrix(matr):
    """Печать матрицы"""
    for i in range(0, len(matr)):
        for j in range(0, len(matr[i])):
            print(matr[i][j], end="\t")
        print()


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print_matrix(matrix)
print("-" * 25)

for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print_matrix(matrix)
