"""
Ссылка на блок-схему:
 https://drive.google.com/file/d/13vPGU_jfXl_IBRviBqtM-F29nmyBBHUW/view?usp=sharing

 Задание 3.
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843.
"""

n = int(input("Введите натуральное число: "))
reverse_number = ""

while n != 0:
    if (n % 10 != 0) or reverse_number != "":
        reverse_number = reverse_number + str(n % 10)
    n = n // 10

print(reverse_number)
