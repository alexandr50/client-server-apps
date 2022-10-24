lst = ['attribute', 'класс', 'функция', 'type']


# функция по нахождению вхожденя всех символов в ascii
def func(word):
    str1 = 'Все символы строки входят в ascii'
    str2 = 'Не все символы строки входят в ascii'
    count = 0
    for i in word:

        if ord(i) < 128:
            count += 1
    return str1 if len(word) == count else str2

print(func(lst[0]))
print(func(lst[1]))
print(func(lst[2]))
print(func(lst[3]))