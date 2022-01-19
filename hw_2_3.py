"""
task_2_3
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата.
"""

import yaml
from pprint import pprint


def write_data_to_yaml(file, data):
    with open(file, 'w', encoding='utf-8') as f_write_yaml:
        my_data_as_string = yaml.dump(data, default_flow_style=True, allow_unicode=True, indent=4)
        f_write_yaml.write(my_data_as_string)

    with open(file, encoding='utf-8') as f_read_yaml:
        content = yaml.load(f_read_yaml, Loader=yaml.FullLoader)
        pprint(content)


if __name__ == '__main__':
    my_file = 'file.yaml'
    my_data = {
        'key_1': ['mobile_phone', 5, 215.99, 'Conor McGregor', 'date'],
        'key_2': 524698,
        'key_3': {'1£': 'mobile_phone', '2¥': 5, '3©': 'Conor McGregor'}
    }
    write_data_to_yaml(my_file, my_data)
