# -*- coding: UTF-8 -*-

import unittest,urllib2,StringIO
from mock import patch
from nokaut import lib

# item = wóda
NOKAUT_RESPONSE = """\
"""
# item = 'a'
NOKAUT_NO_ITEM_RESPONSE = '''/<success>
<items></items>
<total>0</total>
</success>'''

#  key = 1
NOKAUT_WRONG_KEY_RESPONSE = '''/<fail>
<code>101</code>
<message>Invalid API Key</message>
</fail>'''


class NokautExceptionsTest(unittest.TestCase):

    def setUp(self):
        self.nokaut_key = 'a8839b1180ea00fa1cf7c6b74ca01bb5'
        self.nokaut = None

    def tearDown(self):
        self.nokaut_key = None
        self.nokaut = None

    def test_success(self):
        pass

    def test_no_connection_exception(self):
        pass

    def test_no_key_exception(self):
        pass

if __name__ == "__main__":
    unittest.main()