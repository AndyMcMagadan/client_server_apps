"""
task_1_6
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
созданного файла (исходить из того, что вам априори неизвестна кодировка
этого файла!). Затем открыть этот файл и вывести его содержимое на печать.
ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того, в какой кодировке он был создан!
"""

from chardet import detect


def open_and_print(file_name):
    with open(file_name, 'rb') as f:
        content = f.read()
    encoding = detect(content)['encoding']
    print(encoding)

    with open(file_name, 'r', encoding=encoding) as file_1:
        content = file_1.read()
        print(content)


if __name__ == '__main__':
    lines_list = ['сетевое программирование', 'сокет', 'декоратор']
    with open('test.txt', 'w') as file:
        for line in lines_list:
            file.write(f'{line}\n')
    file.close()

    open_and_print('test.txt')
