"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора
на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""

n = int(input("Введите общее количество кустов   "))

d = {}
i = 0
while i < n:
    d[i] = int(input(f'Введите количество ягод на {i+1} кусте(у)   '))
    i +=1

max_count = 0

for i in range(1, len(d) - 1):
    if d[i-1] + d[i] + d[i+1] > max_count: max_count = d[i-1] + d[i] + d[i+1]

if d[0] + d[len(d)-1] + d[len(d)-2] > max_count: max_count = d[0] + d[len(d)-1] + d[len(d)-2]

print(f'Наибольшее количество ягод которое модуль может собрать за раз: {max_count}')