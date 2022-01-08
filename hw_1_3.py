"""
task_1_3
Определить, какие из слов, поданных на вход программы, невозможно
записать в байтовом типе. Для проверки правильности работы кода используйте
значения: «attribute», «класс», «функция», «type»
"""


def check_by_bytes(my_list):
    print(f'Проверка функцией bytes.')
    for word in my_list:
        try:
            print(word, ' --> ', bytes(word, 'ascii'))
        except UnicodeEncodeError:
            print(f'Слово "{word}" невозможно записать байтами.')
    print('=' * 80)


def check_by_encode(my_list):
    print(f'Проверка методом encode.')
    for word in my_list:
        try:
            print(word, ' --> ', word.encode('ascii'))
        except UnicodeEncodeError:
            print(f'Слово "{word}" невозможно записать байтами.')
    print('=' * 80)


def check_by_half_of_ascii(my_list):
    print(f'Проверка символов слова на принадлежность к ASCII.')
    for word in my_list:
        for symbol in word:
            if ord(symbol) > 127:
                print(f'Слово "{word}" невозможно записать байтами.')
                break


if __name__ == '__main__':
    str_1 = 'attribute'
    str_2 = 'класс'
    str_3 = 'функция'
    str_4 = 'type'

    str_list = [str_1, str_2, str_3, str_4]

    check_by_bytes(str_list)
    check_by_encode(str_list)
    check_by_half_of_ascii(str_list)
