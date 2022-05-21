"""
Задание 1: Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные
версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""

import random

SIZE_ARRAY = 10
MIN_ITEM = -100
MAX_ITEM = 99


def sorting(array):
    n = 1
    len_array = len(array) # вводим переменную, для длины массива.
    while n < len_array:
        for i in range(len_array - n):  #уменьшаем количество проходов по циклу на n, так как 1 макс.элемент находиться
            if array[i] < array[i + 1]:  #на первом проходе, второй на втором, и тд.
                array[i + 1], array[i] = array[i], array[i + 1]
        n += 1
    print(array)


data = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARRAY)]
print('Исходный массив:')
print(data)
print('Отсортированный массив:')
sorting(data)
