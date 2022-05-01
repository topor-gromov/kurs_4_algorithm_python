"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

В качестве задачи взял задание 8 занятия 2:
     Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
     Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
import random
import timeit
import cProfile

# Исходный алгоритм. Поиск цифр с использованием целочисленного деления и остатка от деления.
def find_number_1(find_num, count_num):
    sum_result = 0
    for _ in range(0, count_num):
        my_num = random.randint(111, 63999) * random.randint(111, 63999)
        while my_num != 0:
            if my_num % 10 == find_num:
                sum_result += 1
            my_num = my_num // 10

    # print(f'Цифра {find_num} в введённых числах встречается {sum_result} раз(а).')


# find_number(3, 100000)

print(timeit.timeit('find_number_1(3, 10)', number=1000, globals=globals()))  # 0.021276700000000003
print(timeit.timeit('find_number_1(3, 50)', number=1000, globals=globals()))  # 0.10759129999999999
print(timeit.timeit('find_number_1(3, 250)', number=1000, globals=globals()))  # 0.5938707000000001
print(timeit.timeit('find_number_1(3, 1250)', number=1000, globals=globals()))  # 2.6393950999999998
print(timeit.timeit('find_number_1(3, 6250)', number=1000, globals=globals()))  # 13.3956757

cProfile.run('find_number_1(3, 6250)')
"""
62828 function calls in 0.026 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.007    0.007    0.025    0.025 less_4_task_1.py:20(find_number_1)
    12500    0.006    0.000    0.008    0.000 random.py:237(_randbelow_with_getrandbits)
    12500    0.007    0.000    0.015    0.000 random.py:290(randrange)
    12500    0.003    0.000    0.018    0.000 random.py:334(randint)
        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
    12500    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12824    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""


# Использую вместо циклов, целочисленного деления и остатка от деления, число преобразованное в элементы списка.
def find_number_2(find_num, count_num):
    sum_result = 0
    for _ in range(count_num):
        my_num = list(str(random.randint(111, 63999) * random.randint(111, 63999)))
        sum_result += my_num.count(str(find_num))

    #print(f'Цифра {find_num} в введённых числах встречается {sum_result} раз(а).')


#find_number_2(3, 4)


print(timeit.timeit('find_number_2(3, 10)', number=1000, globals=globals()))  # 0.0226384
print(timeit.timeit('find_number_2(3, 50)', number=1000, globals=globals()))  # 0.11878079999999999
print(timeit.timeit('find_number_2(3, 250)', number=1000, globals=globals()))  # 0.6618294
print(timeit.timeit('find_number_2(3, 1250)', number=1000, globals=globals()))  # 2.970911
print(timeit.timeit('find_number_2(3, 6250)', number=1000, globals=globals()))  # 14.9081255

cProfile.run('find_number_2(3, 6250)')

"""
69065 function calls in 0.036 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.036    0.036 <string>:1(<module>)
        1    0.009    0.009    0.036    0.036 less_4_task_1.py:61(find_number_2)
    12500    0.007    0.000    0.009    0.000 random.py:237(_randbelow_with_getrandbits)
    12500    0.012    0.000    0.021    0.000 random.py:290(randrange)
    12500    0.005    0.000    0.025    0.000 random.py:334(randint)
        1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
    12500    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
     6250    0.002    0.000    0.002    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12811    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# Преобразую полученное число в строку и провожу в цикле поиск по элементам строки.
def find_number_3(find_num, count_num):
    sum_result = 0
    for _ in range(count_num):
        my_num = str(random.randint(111, 63999) * random.randint(111, 63999))
        for s in my_num:
            if s == str(find_num):
                sum_result += 1

    # print(f'Цифра {find_num} в введённых числах встречается {sum_result} раз(а).')

# find_number_3(3,4)

print(timeit.timeit('find_number_3(3, 10)', number=1000, globals=globals()))  # 0.0323489
print(timeit.timeit('find_number_3(3, 50)', number=1000, globals=globals()))  # 0.1529459
print(timeit.timeit('find_number_3(3, 250)', number=1000, globals=globals()))  # 0.8236960000000001
print(timeit.timeit('find_number_3(3, 1250)', number=1000, globals=globals()))  # 3.905247
print(timeit.timeit('find_number_3(3, 6250)', number=1000, globals=globals()))  # 21.4682741

cProfile.run('find_number_3(3, 6250)')

"""
62821 function calls in 0.033 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
        1    0.015    0.015    0.033    0.033 less_4_task_1.py:99(find_number_3)
    12500    0.005    0.000    0.008    0.000 random.py:237(_randbelow_with_getrandbits)
    12500    0.007    0.000    0.014    0.000 random.py:290(randrange)
    12500    0.004    0.000    0.019    0.000 random.py:334(randint)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
    12500    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12817    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

"""

Вывод: 
В задании использовал три алгоритма: 
1. С целочисленным делением и остатком от деления.
2. С преобразованием строчных значений цифр числа в элементы списка и подсчёта количества искомых элементов
3. С преобразованием числа в строку и прохождением циклом по данной строке для поиска искомой цифры.

Алгоритм №1 (с использованием целочисленного деления) является более оптимальным с точки зрения скорости 
работы. 

Замеры для всех трёх алгоритмов проводил на значениях: 10, 50, 250, 1250, 6250 (количество генерируемых чисел для
поиска вхождения искомой цифры).

"""