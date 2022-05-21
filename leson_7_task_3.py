"""
Задание 3: Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random

MIN_ITEM = 0
MAX_ITEM = 50

m = int(input('Введите число m, для создания массива размером (2m + 1): '))
size_array = 2 * m + 1

data = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size_array)]
print('Сгенерированный массив:')
print(data)
copy_data = data.copy()

while len(data) > 1:
    min_elem = MAX_ITEM
    max_elem = MIN_ITEM

    for i in range(len(data)):
        if min_elem > data[i]:
            min_elem = data[i]
        if max_elem < data[i]:
            max_elem = data[i]

    data.pop(data.index(min_elem))
    data.pop(data.index(max_elem))

print(f'Медиана = {data[0]}')

# Выводим копию исходного массива. Для наглядности определения медианы отсортируем его.
print('Отсортированная для наглядности копия исходного массива:')
print(sorted(copy_data))

