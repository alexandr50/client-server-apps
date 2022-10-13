import logging
# дефолтный порт по умолчанию
DEFAULT_PORT = 7777

#  ip адресс по умолчанию
DEFAULT_IP_ADDRESS = '127.0.0.1'

# максимальное количество соединений
MAX_CONNECTIONS = 10

# максимальный размер сообщения в байтах
MAX_PACKAGE_LENGTH = 1024

ENCODING = 'utf-8'
LOGGING_LEVEL = logging.DEBUG

# основные ключи
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'