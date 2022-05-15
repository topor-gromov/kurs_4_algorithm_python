"""
Задание 1: Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

count_company = int(input("Введите количество предприятий: "))
company = Counter()
all_profit = 0
for com in range(count_company):
    name_company = input(f'Введите название предприятия №{com + 1} :')
    company_profit = 0
    for i in range(4):
        company_profit += int(input(f'Введите прибыль предприятия "{name_company}" за {i+1} квартал: '))
    company[name_company] = company_profit
    all_profit += company_profit
avg_profit = all_profit / count_company

up_avg = ''
down_avg=''
for key, value in company.items():
    if value > avg_profit:
        if up_avg != '':
            up_avg += '\n' + key + ' - ' + str(value)
        else:
            up_avg += key + ' - ' + str(value)
    elif value < avg_profit:
        if down_avg != '':
            down_avg += '\n' + key + ' - ' + str(value)
        else:
            down_avg += key + ' - ' + str(value)


print(f'\nКомпании чья прибыль выше среднего числа (равного {avg_profit}):')
print(up_avg + '\n')
print(f'Компании чья прибыль ниже среднего числа (равного {avg_profit}):')
print(down_avg + '\n')

