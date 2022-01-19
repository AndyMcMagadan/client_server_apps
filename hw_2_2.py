"""
task_2_2
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON
 с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
"""

import json
from pprint import pprint


def write_order_to_json(file, order):
    with open(file, encoding='utf-8') as f_read:
        content = f_read.read()
        my_orders = json.loads(content)
        my_orders['orders'].append(order)

    with open(file, 'w', encoding='utf-8') as f_write:
        my_orders_as_string = json.dumps(my_orders, sort_keys=True, indent=4, ensure_ascii=False)
        f_write.write(my_orders_as_string)

    # with open(file, 'w', encoding='utf-8') as f_write:
    #     json.dump(my_orders, f_write, sort_keys=True, indent=4, ensure_ascii=False)

    with open(file, 'r', encoding='UTF-8') as f_check:
        content_check = json.load(f_check)
        pprint(content_check)


if __name__ == '__main__':
    my_file = 'orders.json'
    order_1 = {
        'item': 'mobile_phone',
        'quantity': 5,
        'price': 215.99,
        'buyer': 'Conor McGregor',
        'date': '01.01.2022'
    }
    order_2 = {
        'item': 'tablet',
        'quantity': 2,
        'price': 775.99,
        'buyer': 'Andy McMagadan',
        'date': '10.01.2022'
    }

    write_order_to_json(my_file, order_1)
    write_order_to_json(my_file, order_2)
