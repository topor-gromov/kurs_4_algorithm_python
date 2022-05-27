"""
Задание 1:Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

# >>> func("papa")
# 6
# >>> func("sova")
# 9

"""
import hashlib


def find_string(str_a):
    i = 0
    res_set_hash = set()
    res_set_str = set()
    for _ in str_a:
        res = ''
        for char_2 in str_a[i:]:
            res += char_2
            if res != str_a and res != '':
                res_set_hash.add(hashlib.sha1(res.encode()).hexdigest())
                res_set_str.add(res)
        i += 1
    return res_set_hash, res_set_str


my_str = input('Введите исходную строку: ')
my_set_hash, my_set_str = find_string(my_str)

print(f'В строке "{my_str}" {len(my_set_hash)} уникальных подстрок:')
print(my_set_str)

