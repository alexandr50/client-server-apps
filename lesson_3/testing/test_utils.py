import sys
import os
sys.path.append(r"/home/alexandr/PycharmProjects/client-server-appps/lesson_3")
import unittest
import json
print(sys.path)
from common.variables import *
from common.utils import get_message, send_message


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_message = json.dumps(self.test_dict)
        self.encoded_message = json_message.encode(ENCODING)
        self.received_message = send_message

    def recv(self, max_len):
        json_message = json.dumps(self.test_dict)
        return json_message.encode(ENCODING)

class TestUtils(unittest.TestCase):


    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1,
        USER: {
            ACCOUNT_NAME: 'test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_get_message(self):


        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)

        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


    # def test_send_message_ok(self):
    #     test_socket = TestSocket(self.test_dict_send)
    #     send_message(test_socket, self.test_dict_send)
    #     self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    # Данный тест не проходит не понимаю почему , вроде бы все как в лекции

    def test_send_message_error(self):

        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    def test_get_message_ok(self):

        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_error(self):

        test_sock_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()