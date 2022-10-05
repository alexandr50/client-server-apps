import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message

def client_message(message):

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
        }

def main():

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('Номер порта может быть указано только в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    trans = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trans.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    trans.bind((listen_address, listen_port))
    trans.listen(MAX_CONNECTIONS)

    while True:
        client, client_addres = trans.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
















