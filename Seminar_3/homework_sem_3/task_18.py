"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

n = int(input('Введите количество элементов массива...'))

ls = list(map(int, input('Введите через пробел элементы массива...').split()))

x = int(input('Введите число "X"'))

numb = 0

diff = 1000

for i in ls:
    if abs(x - i) < diff and abs(x - i) !=0:
        numb = i
        diff = x - i
print(numb)



