
import sys
import os
sys.path.append(r"/home/alexandr/PycharmProjects/client-server-appps/lesson_3")
import json
import socket
import argparse
import time
import logging
import logs.config_client_log
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message


CLIENT_LOGGER = logging.getLogger('client')
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out

def process_answer(message):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError

def create_arg_parser():
    """
    Создаём парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser



def main():

    try:
        parser = create_arg_parser()
        namespace = parser.parse_args(sys.argv[1:])
        server_address = namespace.addr
        server_port = namespace.port
        # server_address = sys.argv[1]
        # server_port = int(sys.argv[2])
        if not 1023 < server_port < 65536:
            CLIENT_LOGGER.critical(
                f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
                f' Допустимы адреса с 1024 до 65535. Клиент завершается.')
            sys.exit(1)

        CLIENT_LOGGER.info(f'Запущен клиент с парамертами: '
                       f'адрес сервера: {server_address} , порт: {server_port}')
    finally:
        pass


    trans = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trans.connect((server_address, server_port))
    mess_to_server = create_presence()
    send_message(trans, mess_to_server)
    try:
        answer = process_answer(get_message(trans))
        print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Не удалось декодировать полученную Json строку.')
    except (ValueError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()












