from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')



with open('test_file.txt', 'rb') as file:
    result = file.read()
encoding = detect(result)['encoding']
print(encoding)

with open('test_file.txt', 'r', encoding=encoding) as file:
    result = file.read()
print(result)