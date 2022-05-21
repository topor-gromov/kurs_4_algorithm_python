"""
Задание 2: Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE_ARRAY = 10
MIN_ITEM = 0
MAX_ITEM = 50


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_slice = merge_sort(array[:mid])
    right_slice = merge_sort(array[mid:])
    result = []
    i = 0
    j = 0
    while len(left_slice) > i and len(right_slice) > j:
        if left_slice[i] < right_slice[j]:
            result.append(left_slice[i])
            i += 1
        else:
            result.append(right_slice[j])
            j += 1
    result.extend(left_slice[i:])
    result.extend(right_slice[j:])
    return result


data = [round(random.uniform(MIN_ITEM, MAX_ITEM), 8) for _ in range(SIZE_ARRAY)]
print('Исходный массив:')
print(data)
print('Отсортированный массив:')
print(merge_sort(data))
