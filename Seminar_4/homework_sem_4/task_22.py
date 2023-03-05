"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

"""

n = int(input("Введите количество элементов первого списка...   "))

m = int(input("Введите количество элементов второго списка...   "))

set_one = {int(i) for i in input("Введите элементы первого списка через пробел   ").split()}

set_two = {int(i) for i in input("Введите элементы второго списка через пробел   ").split()}

result_set = sorted(set_one & set_two)

print(f'Элементы содержащиеся в двух свписках по порядку : ', end=" ")
print(*result_set, sep=", ")