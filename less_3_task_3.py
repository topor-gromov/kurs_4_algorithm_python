"""
Задание 3:
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

# решение задачи
min_elem = array[0]
max_elem = array[0]
min_elem_ind = 0
max_elem_ind = 0
i = 0
for item in array:
    if item > max_elem:
        max_elem = item
        max_elem_ind = i
    if item < min_elem:
        min_elem = item
        min_elem_ind = i
    i += 1

array[max_elem_ind], array[min_elem_ind] = array[min_elem_ind], array[max_elem_ind]

print(f'Максимальный элемент со значением: {max_elem}, находится по индексу: {max_elem_ind}.')
print(f'Максимальный элемент со значением: {min_elem}, находится по индексу: {min_elem_ind}.\n')
print(f'Преобразованный массив: {array}')
