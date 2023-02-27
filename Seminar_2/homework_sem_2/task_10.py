"""
Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

"""

n = int(input("Введите общее количество монеток..."))

# счётчик количества монеток с орлом
count_1 = 0

# счётчик количества монеток с решкой
count_0 = 0

for i in range(n):
    temp = int(input("Введите 0(решка) или 1(орёл)"))
    if temp:
        count_1 += 1
    else:
        count_0 += 1
if count_1 > count_0:
    print(f'Необходимо перевернуть {count_0} монет.')
else:
    print(f'Необходимо перевернуть {count_1} монет.')
