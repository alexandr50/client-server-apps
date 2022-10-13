import sys
sys.path.append(r"/home/alexandr/PycharmProjects/client-server-appps/lesson_3")
import unittest
from common.variables import *
from client import create_presence, process_answer

class Testclass(unittest.TestCase):

    def test_200_answer(self):

        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    def test_400_answer(self):
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_presense_guest(self):
        """ проверка присутствия(Guest)
        """
        test = create_presence()
        test[TIME] = 2  
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}})





if __name__ == '__main__':
    unittest.main()