"""
Задание 9:
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

# постановка задачи
import random

SIZE_M = 4
SIZE_N = 6
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]

# решение задачи
STEP = 5
min_column = [MAX_ITEM] * len(matrix[0])
print(f'Исходная матрица {SIZE_N}x{SIZE_M}:')

for line in matrix:
    for i, item in enumerate(line):
        if min_column[i] > item:
            min_column[i] = item
        print(f'{item:>{STEP}}', end='')
    print()
print(f'Массив минимальных значений в столбцах матрицы:')

max_elem = MIN_ITEM
for item in min_column:
    if item > max_elem:
        max_elem = item
    print(f'{item:>{STEP}}', end='')
print()

print(f'Максимальный элемент среди минимальных элементов матрицы: {max_elem}.')
