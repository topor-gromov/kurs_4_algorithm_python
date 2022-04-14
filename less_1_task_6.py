"""
Ссылка на блок-схему:
https://drive.google.com/file/d/1QLaGat4iiq76-gGtx9evRq1wuKPqbQzc/view?usp=sharing

Задание 6: Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

number_letter = int(input("Введите номер буквы алфавита, в промежутке от 1 до 26: "))

a = number_letter + 96
letter = chr(a)

print(f'Буквой алфавита под номером {number_letter}, является буква: {letter}')
