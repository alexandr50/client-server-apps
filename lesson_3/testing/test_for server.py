import sys
sys.path.append(r"/home/alexandr/PycharmProjects/client-server-appps/lesson_3")
import unittest
from server import client_message
from common.variables import *

class TestClass(unittest.TestCase):
    failed_dict = {RESPONSE: 400, ERROR: 'Bad Request'}
    success_dict_guest = {'error': '200:OK', 'msg': 'Welcome, Гость', 'response': 200}
    success_dict_auth_user = {'error': '200:OK', 'msg': 'Welcome, AUTH_USER', 'response': 200}

    def test_fail_message_object(self):

        self.assertEqual(client_message('AUTH_USER'), self.failed_dict)

    def test_no_key_action(self):

        self.assertEqual(client_message({TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.failed_dict)

    def test_no_key_time(self):

        self.assertEqual(client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.failed_dict)

    def test_no_key_user(self):

        self.assertEqual(client_message({ACTION: PRESENCE, TIME: '2'}), self.failed_dict)

    def test_wrong_action_value(self):

        self.assertEqual(client_message(
            {ACTION: 'abrakadabra', TIME: '2', USER: {ACCOUNT_NAME: 'Guest'}}), self.failed_dict)



if __name__ == '__main__':
    unittest.main()
