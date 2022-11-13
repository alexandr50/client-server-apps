import json

def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)

    with open('orders.json', 'w', encoding='utf-8') as file_in:
        lst = data['orders']
        result = {
            'item': item,
            'quatity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        lst.append(result)
        json.dump(data, file_in, indent=4)




print(write_order_to_json('laptop', '2', '40000','alex', '12.12.12'))
print(write_order_to_json('phone', '5', '50000', 'fill', '12.12. 12'))
