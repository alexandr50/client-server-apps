import csv
import re
import chardet
from chardet import detect


def get_data():
    product_lst = []
    name_lst = []
    code_lst = []
    type_lst = []
    result_lst = []

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file:
            data_b = file.read()
            res = chardet.detect(data_b)
            data = data_b.decode(res['encoding'])

        prod_search = re.compile(r'Изготовитель системы:\s*\S*')
        product_lst.append(prod_search.findall(data)[0].split()[2])

        name_search = re.compile(r'Windows\s*\S*')
        name_lst.append(name_search.findall(data)[0])

        code_search = re.compile(r'Код продукта:\s*\S*')
        code_lst.append(code_search.findall(data)[0].split()[2])

        type_search = re.compile(r'Тип системы:\s*\S*')
        type_lst.append(type_search.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    result_lst.append(headers)

    data_ = [product_lst, name_lst, code_lst, type_lst]

    res = []
    n = len(data_)
    m = len(data_[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp += [data_[i][j]]
        res += [tmp]
    return res


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report_.csv')
