"""
task_6
1. Продолжая задачу логирования, реализовать декоратор @log, фиксирующий обращение
к декорируемой функции. Он сохраняет ее имя и аргументы.
2. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная.
Если имеется такой код:
@log
def func_z():
 pass

def main():
 func_z()
...в логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
"""

"""Программа-клиент"""

import sys
import json
import socket
import time
import argparse
import logging
import logs.config_client_log
from common.variables import ACTION, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, ERROR, PRESENCE
from common.utils import get_message, send_message
# from common.utils_for_log_as_class import get_message, send_message
from errors import ReqFieldMissingError
from decos import log

# Инициализация клиентского логера
LOGGER = logging.getLogger('client')


@log
def create_presence(account_name='Guest'):
    """Функция генерирует запрос о присутствии клиента"""
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out
