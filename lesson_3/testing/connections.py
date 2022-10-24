from socket import socket,  AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import sys

sys.path.append('../')
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, \
    DEFAULT_PORT, DEFAULT_IP_ADDRESS



trans = socket(AF_INET, SOCK_STREAM)
trans.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
trans.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
trans.listen(MAX_CONNECTIONS)


trans_client = socket(AF_INET, SOCK_STREAM)
trans_client.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))


client, address = trans.accept()
message = b'hi'
trans_client.send(message)
answer = client.recv(1024)
print(answer)

trans.close()
trans_client.close()
client.close()