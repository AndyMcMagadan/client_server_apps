"""
task_1_2
Каждое из слов «class», «function», «method» записать в байтовом типе.
Сделать это необходимо в автоматическом, а не ручном режиме с помощью добавления
литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode
и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def string_in_bites(my_list):
    for elem in my_list:
        b_string = eval(f"b'{elem}'")
        print(b_string)
        print('type: ', type(b_string))
        print('length in bytes: ', len(b_string))
        print('=' * 80)


if __name__ == '__main__':
    str_1 = 'class'
    str_2 = 'function'
    str_3 = 'method'

    str_list = [str_1, str_2, str_3]
    string_in_bites(str_list)
