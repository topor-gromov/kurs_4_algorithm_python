"""
Ссылка на блок-схему:
 https://drive.google.com/file/d/13vPGU_jfXl_IBRviBqtM-F29nmyBBHUW/view?usp=sharing

 Задание 8.
     Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
     Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

find_num = int(input("Введите цифру для поиска: "))
count_num = int(input("Введите количество чисел: "))
sum_result = 0

for i in range(0, count_num):
    my_num = int(input(f'Введите число №{i+1}: '))
    while my_num != 0:
        if my_num % 10 == find_num:
            sum_result += 1
        my_num = my_num // 10

print(f'Цифра {find_num} в введённых числах встречается {sum_result} раз(а).')

