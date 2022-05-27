"""
Задание 2:  Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.

"""

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def __repr__(self):
        return f'{self.value}\n{self.left} - {self.right}\n'


def get_code(root, code_dict=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        code_dict[root.value] = code
        return code_dict

    get_code(root.left, code_dict, code + '0')
    get_code(root.right, code_dict, code + '1')

    return code_dict


def get_tree(fun_str):
    letter = Counter(fun_str)

    if len(letter) == 1:
        node = Node(None)
        node.left = Node((list(letter.keys()))[0])
        node.right = Node(None)
        letter = {node: 1}

    while len(letter) > 1:
        node = Node(None)
        tmp_list = letter.most_common()[:-3:-1]
        if isinstance(tmp_list[0][0], str):
            node.left = Node(tmp_list[0][0])
        else:
            node.left = tmp_list[0][0]

        if isinstance(tmp_list[1][0], str):
            node.right = Node(tmp_list[1][0])
        else:
            node.right = tmp_list[1][0]

        letter.pop(tmp_list[0][0])
        letter.pop(tmp_list[1][0])
        letter[node] = tmp_list[0][1] + tmp_list[1][1]

    return (list(letter.keys()))[0]


my_str = input('Введите строку для обработки: ')
if len(my_str) > 0:
    code_d = get_code(get_tree(my_str))
else:
    print('Вы не ввели строку для обработки.')

print(f'Таблица шифрования: {code_d}')

result = ''
for elem in my_str:
    result += code_d[elem]

print('Сжатая строка: ', result)
