"""
Задание 7:
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
собой (оба являться минимальными), так и различаться.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

# решение задачи
min_elem_1 = array[0]
min_elem_2 = array[0]
flag_find_min = False

for i in range(len(array)):
    if array[i] < min_elem_1:
        min_elem_2 = min_elem_1
        min_elem_1 = array[i]
        flag_find_min = True
    if array[i] < min_elem_2 and not flag_find_min:
        min_elem_2 = array[i]
    flag_find_min = False

print(f'Минимальные элементы массива: {min_elem_1}, {min_elem_2}')
