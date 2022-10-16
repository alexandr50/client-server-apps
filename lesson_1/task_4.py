lst = ['разработка', 'администрирование', 'protocol', 'standard']

arr1 = []

for i in lst:
    res = i.encode('utf-8')
    arr1.append(res)

arr2 = []

for i in arr1:
    res = i.decode('utf-8')
    arr2.append(res)

print(arr1)
print(arr2)