"""
task_1_4
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное
преобразование (используя методы encode и decode).
"""


def string_to_bytes(my_list):
    bytes_list = []
    for word in my_list:
        b_word = word.encode('utf-8')
        print(b_word)
        bytes_list.append(b_word)
    return bytes_list


def bytes_to_string(my_list):
    str_list.clear()
    for elem in my_list:
        str_word = elem.decode('utf-8')
        print(str_word)
        str_list.append(str_word)
    return str_list


if __name__ == '__main__':
    str_1 = 'разработка'
    str_2 = 'администрирование'
    str_3 = 'protocol'
    str_4 = 'standard'

    str_list = [str_1, str_2, str_3, str_4]

    result = string_to_bytes(str_list)
    print('=' * 80)
    bytes_to_string(result)
