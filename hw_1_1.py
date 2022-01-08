"""
task_1_1
Каждое из слов «разработка», «сокет», «декоратор» представить
в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
Unicode и также проверить тип и содержимое переменных.
"""


def print_value_and_type(my_list):
    for word in my_list:
        print(word)
        print(type(word))
    print('=' * 80)


if __name__ == '__main__':
    word_1 = 'разработка'
    word_2 = 'сокет'
    word_3 = 'декоратор'
    words_list = [word_1, word_2, word_3]

    print_value_and_type(words_list)

    word_1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
    word_2_unicode = '\u0441\u043e\u043a\u0435\u0442'
    word_3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    words_list_unicode = [word_1_unicode, word_2_unicode, word_3_unicode]

    print_value_and_type(words_list_unicode)
