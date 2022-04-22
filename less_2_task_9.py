"""
 Ссылка на блок-схему:
 https://drive.google.com/file/d/13vPGU_jfXl_IBRviBqtM-F29nmyBBHUW/view?usp=sharing

 Задание 9.
 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def summ_number(num):
    if num // 10 == 0:
        return num % 10
    else:
        return (num % 10) + summ_number(num // 10)


sum_num = 0
res_num = 0

while True:
    my_num = int(input("Введите натуральное число: "))
    if my_num != 0:
        result = summ_number(my_num)
        if result > sum_num:
            sum_num = result
            res_num = my_num
    else:
        break

print(f'Число {res_num} является наибольшим по сумме цифр. Сумма его цифр равна {sum_num}.')
