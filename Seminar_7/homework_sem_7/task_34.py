"""
задача 34:  винни-пух попросил вас посмотреть,
есть ли в его стихах ритм. поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, вам стоит написать программу.
винни-пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
в каждой фразе стихотворения одинаковое. фраза может состоять из одного слова,
если во фразе несколько слов, то они разделяются дефисами. фразы отделяются друг от друга пробелами.
стихотворение  винни-пух вбивает в программу с клавиатуры. в ответе напишите “парам пам-пам”,
если с ритмом все в порядке и “пам парам”, если с ритмом все не в порядке

*пример:*

**ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **вывод:** парам пам-пам
"""

vowel = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я')


def parampampam(phrase: str) -> int:
    count = 0
    for i in phrase:
        if i.lower() in vowel:
            count += 1
    return count


phrase = list(map(parampampam, input('Введите фразу...  ').split()))

print(phrase)

# if sum(phrase)/len(phrase) == phrase[0]:
#     print('парам пам-пам')
# else:
#     print('пам парам')

if len(set(phrase)) == 1:
    print('парам пам-пам')
else:
    print('пам парам')