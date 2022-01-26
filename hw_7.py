"""Программа-клиент"""

import sys
import json
import socket
import time
import argparse
import logging
import logs.config_client_log
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, \
    ACTION, TIME, USER, ACCOUNT_NAME, SENDER, PRESENCE, RESPONSE, ERROR, MESSAGE, MESSAGE_TEXT
from common.utils import get_message, send_message
from errors import ReqFieldMissingError, ServerError
from decos import log

# Инициализация клиентского логера
LOGGER = logging.getLogger('client')


@log
def message_from_server(message):
    """Функция - обработчик сообщений других пользователей, поступающих с сервера"""
    if ACTION in message and message[ACTION] == MESSAGE and \
            SENDER in message and MESSAGE_TEXT in message:
        print(f'Получено сообщение от пользователя '
              f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
        LOGGER.info(f'Получено сообщение от пользователя '
                    f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
    else:
        LOGGER.error(f'Получено некорректное сообщение с сервера: {message}')
