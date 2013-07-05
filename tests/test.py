import unittest
import sys
sys.path.append('../nokaut')
import lib

NOKAUT_RESPONSE = """\
mama
"""

NOKAUT_NO_ITEM_RESPONSE = ''


NOKAUT_WRONG_KEY_RESPONSE = ''


class NokautExceptionsTest(unittest.TestCase):

    def __init__(self):
        self.nokaut = None

    def tearDown(self):
        self.nokaut = None

    def wrong_key_exception_test(self):
        pass

    def no_connection_exception_test(self):
        pass

    def no_key_exception_test(self):
        pass

if __name__ == '__main__':
    unittest.main()