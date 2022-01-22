"""
task_5_1
В директории проекта создать каталог log, в котором для клиентской и серверной сторон
в отдельных модулях формата client_log_config.py и server_log_config.py создать логгеры;
"""

import socket
import sys
import json


def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)


if __name__ == '__main__':
    # Порт поумолчанию для сетевого ваимодействия
    DEFAULT_PORT = 7777
    # IP адрес по умолчанию для подключения клиента
    DEFAULT_IP_ADDRESS = '127.0.0.1'
    # Максимальная очередь подключений
    MAX_CONNECTIONS = 5
    # Максимальная длинна сообщения в байтах
    MAX_PACKAGE_LENGTH = 1024
    # Кодировка проекта
    ENCODING = 'utf-8'

    # Прококол JIM основные ключи:
    ACTION = 'action'
    TIME = 'time'
    USER = 'user'
    ACCOUNT_NAME = 'account_name'

    # Прочие ключи, используемые в протоколе
    PRESENCE = 'presence'
    RESPONSE = 'response'
    ERROR = 'error'
    RESPONDEFAULT_IP_ADDRESSSE = 'respondefault_ip_addressse'
