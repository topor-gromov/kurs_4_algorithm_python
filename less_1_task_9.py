"""
Ссылка на блок-схему:
https://drive.google.com/file/d/1QLaGat4iiq76-gGtx9evRq1wuKPqbQzc/view?usp=sharing

Задание 9: Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print("Необходимо ввести три разных числа.")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if b < a < c or b > a > c:
    average = a
elif a < b < c or a > b > c:
    average = b
else:
    average = c

print(f'Число {average} является средним из трёх введённых.')