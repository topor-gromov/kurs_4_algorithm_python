"""
Задание 6:
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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
start_ind = 0
end_ind = 0
i = 0
for item in array:
    if item > max_elem:
        max_elem = item
        end_ind = i

    if item < min_elem:
        min_elem = item
        start_ind = i
    i += 1

print(f'Максимальный элемент со значением: {max_elem}, находится по индексу: {end_ind}.')
print(f'Максимальный элемент со значением: {min_elem}, находится по индексу: {start_ind}.\n')

if start_ind > end_ind:
    start_ind, end_ind = end_ind, start_ind

sum_elem = 0
for i in range(start_ind + 1, end_ind):
    sum_elem += array[i]

print(f'Сумма элементов расположенных между минимальным и максимальным элементами равна: {sum_elem}')
