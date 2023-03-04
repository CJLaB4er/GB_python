"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
"""
one_point = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'.split(", ")

two_point = 'D, G, Д, К, Л, М, П, У'.split(", ")

three_point = 'B, C, M, P, Б, Г, Ё, Ь, Я'.split(", ")

four_point = 'F, H, V, W, Y, Й, Ы'.split(", ")

five_point = 'K, Ж, З, Х, Ц, Ч'.split(", ")

eight_point = 'J, X, Ш, Э, Ю'.split(", ")

ten_point = 'Q, Z, Ф, Щ, Ъ'.split(", ")


word = input("Введите слово...")



"""
Здесь описан алгоритм определения языка введенного слова. В моем решении в нём нет необходимости.

lang = True # при значении True язык является русским, False - en
if ord(word[0].lower()) in range(97, 123):
    lang = False
"""
count = 0

for i in word:
    i = i.upper()
    if i in one_point: count += 1
    elif i in two_point: count += 2
    elif i in three_point: count += 3
    elif i in four_point: count += 4
    elif i in five_point: count += 5
    elif i in eight_point: count += 8
    elif i in ten_point: count += 10
print(count)