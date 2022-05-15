"""
Задание 2: Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь
ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из
примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import deque, Counter


def elem_summ(elem_1, elem_2):
    hex_value = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
    if len(elem_2) > len(elem_1):
        elem_1, elem_2 = elem_2, elem_1

    deque_a = deque(elem_1.upper())
    deque_b = deque(elem_2.upper())
    deque_c = deque()
    transit = 0

    while len(deque_a) != 0:
        num_hex_1 = hex_value[deque_a.pop()]
        if len(deque_b) != 0:
            num_hex_2 = hex_value[deque_b.pop()]
        else:
            num_hex_2 = 0

        hex_s = num_hex_1 + num_hex_2 + transit

        transit = hex_s // 16
        hex_s = hex_s % 16

        if hex_s <= 9:
            deque_c.appendleft(hex_s)
        elif hex_s == 10:
            deque_c.appendleft('A')
        elif hex_s == 11:
            deque_c.appendleft('B')
        elif hex_s == 12:
            deque_c.appendleft('C')
        elif hex_s == 13:
            deque_c.appendleft('D')
        elif hex_s == 14:
            deque_c.appendleft('E')
        else:
            deque_c.appendleft('F')

    if transit != 0:
        deque_c.appendleft(transit)
    return deque_c


def elem_prod(elem_1, elem_2):
    hex_value = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
    if len(elem_2) > len(elem_1):
        elem_1, elem_2 = elem_2, elem_1

    deque_b = deque(elem_2.upper())
    deque_c = deque()

    temp_result = ''
    count_categ = ''

    while len(deque_b) > 0:
        deque_a = deque(elem_1.upper())
        num_hex_2 = hex_value[deque_b.pop()]
        transit = 0
        while len(deque_a) > 0:
            num_hex_1 = hex_value[deque_a.pop()]
            hex_prod = (num_hex_1 * num_hex_2) + transit
            transit = hex_prod // 16
            hex_prod = hex_prod % 16

            if hex_prod <= 9:
                temp_result = str(hex_prod) + temp_result
            elif hex_prod == 10:
                temp_result = 'A' + temp_result
            elif hex_prod == 11:
                temp_result = 'B' + temp_result
            elif hex_prod == 12:
                temp_result = 'C' + temp_result
            elif hex_prod == 13:
                temp_result = 'D' + temp_result
            elif hex_prod == 14:
                temp_result = 'E' + temp_result
            else:
                temp_result = 'F' + temp_result
        if transit != 0:
            temp_result = str(transit) + temp_result

        deque_c.append(temp_result)
        count_categ += '0'  # переменная для разряда чисел
        temp_result = count_categ
        result_for_summ_element = ''

        if len(deque_c) > 1:  # если в очереди больше одного элемента (два) складываем их между собой
            elem_for_summ_1 = deque_c.pop()
            elem_for_summ_2 = deque_c.pop()
            elem_for_sum = elem_summ(elem_for_summ_1, elem_for_summ_2)
            while len(elem_for_sum) > 0:  # результат сложения в виде очереди соединяем в одно значение
                result_for_summ_element += str(elem_for_sum.popleft())
            deque_c.append(result_for_summ_element)
    res = deque_c.pop()
    deque_res = deque(res)  # разделяем результат на элементы.
    return deque_res


a = input("Введите первое шестнадцатеричное число: ")
b = input("Введите второе шестнадцатеричное число: ")

# Сумма чисел
s = elem_summ(a, b)
result_summ = ''
while len(s) > 0:
    result_summ += str(s.popleft())

print(f'Результат сложения введённых шестнадцатеричных чисел: {result_summ}')

# произведение чисел.
p = elem_prod(a, b)
result_prod = ''
while len(p) > 0:
    result_prod += str(p.popleft())

print(f'Результат произведения введённых шестнадцатеричных чисел: {result_prod}')

