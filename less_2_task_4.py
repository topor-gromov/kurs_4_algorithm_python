"""
Ссылка на блок-схему:
 https://drive.google.com/file/d/13vPGU_jfXl_IBRviBqtM-F29nmyBBHUW/view?usp=sharing

 Задание 4.
 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

n = int(input("Введите количество элементов n: "))

elem = 1
summ_elem = 0

for i in range(0,n):
    summ_elem += elem
    elem = elem / -2

print(f'Сумма элементов ряда, для n={n}, равна {summ_elem}')
