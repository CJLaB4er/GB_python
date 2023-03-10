"""
Задача 3: Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

# Программа проверяет на "счастливость" билетики с любым количеством цифр.

numb = input('Введите номер билетика...')

mid = len(numb) // 2

sum = 0

for i in range(mid):
    sum += int(numb[i])

if len(numb)%2 == 0: # Если в билете чётное количество цифр, то идёт стандартная проверка
    for i in range(mid, len(numb)):
        sum -= int(numb[i])

else: # Если в бителе нечётное количество цифр, то считаются цифры слева и справа от центрального.
    for i in range(mid + 1, len(numb)):
        sum -= int(numb[i])

if sum == 0:
    print("Билетик счастливый!")
else:
    print("Билетик Не счастливый!")