"""
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
"""

stroka = input().lower().split()
print(type(stroka))
print(stroka)
result = set(stroka)
print(len(result))