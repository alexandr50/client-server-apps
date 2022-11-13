import sys
import logging
import logs.config_server_log
import logs.config_client_log
import traceback
import inspect

def log(func):
    def wrapper(*args, **kwargs):
        name_log = 'server' if 'server.py' in sys.argv[0] else 'client'
        LOGGER = logging.getLogger(name_log)
        result = func(*args, **kwargs)
        LOGGER.debug(
            f'Была вызвана функция {func.__name__} с параметрами {args} {kwargs}.'
            f'Вызов из модуля {func.__module__}.'
            f'Вызов из функции {inspect.stack()[1][1]}', stacklevel=2)
        return result
    return wrapper
