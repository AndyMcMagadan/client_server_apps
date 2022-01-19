"""
task_2_1
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt,
info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""
import re
import csv

import chardet


def get_data(f_list):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for file in f_list:
        with open(file, 'rb') as f_obj:
            data_bytes = f_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s\S*')
        os_name_list.append(os_name_reg.findall(data)[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    data_for_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for i in range(len(data_for_rows[0])):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv(file_w, f_list):
    main_data = get_data(f_list)

    with open(file_w, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerows(main_data)


if __name__ == '__main__':
    file_1 = "info_1.txt"
    file_2 = "info_2.txt"
    file_3 = "info_3.txt"
    files_list = [file_1, file_2, file_3]

    write_to_csv('data_write.csv', files_list)
