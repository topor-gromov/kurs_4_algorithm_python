"""
Задание 5:
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

# решение задачи
max_negative_num = MIN_ITEM
max_negative_num_ind = 0

for i in range(len(array)):
    if 0 > array[i] > max_negative_num:
        max_negative_num = array[i]
        max_negative_num_ind = i

print(f'Максимальный отрицательный элемент: {max_negative_num}, индекс элемента: {max_negative_num_ind}.')
