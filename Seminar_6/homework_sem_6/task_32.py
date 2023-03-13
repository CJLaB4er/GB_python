"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

from random import randint


def create_random_list(n):
    temp_list = []
    for i in range(n):
        temp_list.append(randint(1, 25))
    return temp_list

def index_in_list(insp_list):
    temp_list = []
    min_x = int(input('Введите минимальное значение '))
    max_x = int(input('Введите максимальное значение '))
    for i in range(len(insp_list)):
        if min_x <= insp_list[i] <= max_x:
            temp_list.append(i)
    return temp_list


inspect_list = create_random_list(int(input('Введите количество случайных элементов исследуемого массива  ')))

index_list = index_in_list(inspect_list)

print(inspect_list)
print('Значения исходного массива под следующими индесками удовлетворяют условиям задачи:', end=' ')

for i in index_list:
    print(f'{i}({inspect_list[i]})', end='; ')
