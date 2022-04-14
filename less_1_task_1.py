"""
Ссылка на блок-схему:
https://drive.google.com/file/d/1QLaGat4iiq76-gGtx9evRq1wuKPqbQzc/view?usp=sharing

Задание 1:
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input("Введите целое трёхзначное число: "))

b = a // 100
a = a - (b * 100)
c = a // 10
a = a - (c * 10)
summ = a + b + c
prod = a * b * c

print(f'Сумма цифр равна: {summ}. Произведение цифр равно: {prod}')
