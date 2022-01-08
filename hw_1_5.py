"""
task_1_5
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтового в строковый (предварительно определив кодировку выводимых сообщений).
"""

import subprocess
import chardet
import platform


def string_result_ping_url(my_urls):
    global result
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    print('=' * 80)
    for url in my_urls:
        args = ['ping', param, '2', url]
        result_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in result_ping.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))
        print(result)
        print('=' * 80)


if __name__ == '__main__':
    urls = ['yandex.ru', 'youtube.com']
    string_result_ping_url(urls)
