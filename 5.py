# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# count=int(input('Введите количество организаций: '))
# if count > 0:
#     org_dict = dict()
#     summ_all_org = 0
#     for i in range(count):
#         org_name = input(f'Введите название {i+1}-го предприятия: ')
#         summ_one_org = 0
#         for j in range(4):
#             summ_one_org += float(input(f'Введите прибыль за {j+1}-й квартал: '))
#         summ_all_org += summ_one_org
#         org_dict[org_name] = summ_one_org
#     srednee = summ_all_org/(count)
#     print(f'Средняя прибыль у всех предприятий: {srednee}')
#     print()
#     print('Организации и их прибыль ВЫШЕ2 средней:')
#     for k, v in org_dict.items():
#         if v > srednee:
#             print(f'Организация {k} имеет прибыль за год: {v}')
#     print()
#     print('Организации и их прибыль НИЖЕ средней:')
#     for k, v in org_dict.items():
#         if v < srednee:
#             print(f'Организация {k} имеет прибыль за год: {v}')
#

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections




from collections import defaultdict
from collections import deque


def my_dex(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def my_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = my_dex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = my_dex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')