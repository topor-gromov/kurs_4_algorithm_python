"""
Задание 2:
 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.
- Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

import timeit
import cProfile


# sieve_1 Вариант из методички. Без оптимизации.

def sieve_1(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b
    # print(b)


# sieve_2. Для оптимизации алгоритма использовал цикл for вместо цикла while.
def sieve_2(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    for i in range(2, n):  # Использовал цикл for вместо цикла while
        if a[i] != 0:
            j = i * 2
            for z in range(j, n, i):  # цикл for вместо цикла while
                a[z] = 0

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b


# функция внутри себя вызывает sieve_1 (функция без оптимизации).
def sieve_number_1(n):
    find_number = False
    m = n * 2
    while not find_number:
        b = sieve_1(m)
        if len(b) == n:
            find_number = True
        else:
            m += 1
    sieve_number = b[n - 1]
    # print(sieve_number)


# функция внутри себя вызывает sieve_2 (функция с оптимизацией).
def sieve_number_2(n):
    find_number = False

    # При n<13 необходимо решето более чем n*2, при n>13 решето более n*3
    # Использую для оптимизации алгоритма.
    if n < 13:
        m = n * 2
    else:
        m = n * 3
    while not find_number:
        b = sieve_2(m)
        if len(b) == n:
            find_number = True
        else:
            m += 1
    sieve_number = b[n - 1]
    # print(sieve_number)


# - Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

def prime(n):
    a = [2]
    z = 2
    while len(a) != n:
        z += 1
        flag = False
        for item in a:
            if z % item == 0:
                flag = True
                break
        if not flag:
            a.append(z)
    # print(a)


# prime(1000)
# sieve_1(1000)
# sieve_2(1000)
# sieve_number_1(128)
# sieve_number_2(128)

# Алгоритмы «Решето Эратосфена» медленные, поэтому взял небольшие значения для проверки
print(timeit.timeit('sieve_number_1(8)', number=1000, globals=globals()))  # 0.0226246
print(timeit.timeit('sieve_number_1(16)', number=1000, globals=globals()))  # 0.23384150000000004
print(timeit.timeit('sieve_number_1(32)', number=1000, globals=globals()))  # 2.4647866
print(timeit.timeit('sieve_number_1(64)', number=1000, globals=globals()))  # 12.730703
print(timeit.timeit('sieve_number_1(128)', number=1000, globals=globals()))  # 81.6839792

cProfile.run('sieve_number_1(128)')

"""
43664 function calls in 0.067 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.067    0.067 <string>:1(<module>)
      465    0.063    0.000    0.066    0.000 less_4_task_2.1.py:17(sieve_1)
        1    0.000    0.000    0.067    0.067 less_4_task_2.1.py:60(prime_number_1)
        1    0.000    0.000    0.067    0.067 {built-in method builtins.exec}
      465    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    42730    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 
"""

print(timeit.timeit('sieve_number_2(8)', number=1000, globals=globals()))  # 0.023109
print(timeit.timeit('sieve_number_2(16)', number=1000, globals=globals()))  # 0.0870753
print(timeit.timeit('sieve_number_2(32)', number=1000, globals=globals()))  # 1.1907826
print(timeit.timeit('sieve_number_2(64)', number=1000, globals=globals()))  # 7.2355564999999995
print(timeit.timeit('sieve_number_2(128)', number=1000, globals=globals()))  # 52.4547113

cProfile.run('sieve_number_2(128)')

"""
35090 function calls in 0.048 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.048    0.048 <string>:1(<module>)
      337    0.045    0.000    0.048    0.000 less_4_task_2.1.py:41(sieve_2)
        1    0.000    0.000    0.048    0.048 less_4_task_2.1.py:73(prime_number_2)
        1    0.000    0.000    0.048    0.048 {built-in method builtins.exec}
      337    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    34412    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('prime(80)', number=1000, globals=globals()))  # 0.2056057
print(timeit.timeit('prime(160)', number=1000, globals=globals()))  # 0.8921477000000001
print(timeit.timeit('prime(320)', number=1000, globals=globals()))  # 3.500357
print(timeit.timeit('prime(640)', number=1000, globals=globals()))  # 11.303662
print(timeit.timeit('prime(1280)', number=1000, globals=globals()))  # 47.761097400000004

cProfile.run('prime(1280)')
"""
11741 function calls in 0.043 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.043    0.043 <string>:1(<module>)
        1    0.041    0.041    0.042    0.042 less_4_task_2.py:94(prime)
        1    0.000    0.000    0.043    0.043 {built-in method builtins.exec}
    10458    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     1279    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
