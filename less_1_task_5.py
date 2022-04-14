"""
Ссылка на блок-схему:
https://drive.google.com/file/d/1QLaGat4iiq76-gGtx9evRq1wuKPqbQzc/view?usp=sharing

Задание 5.
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

letter1 = input("Введите первую букву: ")
letter2 = input("Введите вторую букву: ")

a = ord(letter1)
b = ord(letter2)

if a < b:
    c = (b - a) - 1
else:
    c = (a - b) - 1

print(f'Между буквами {letter1} и {letter2} расположено {c} букв(а/ы).')
