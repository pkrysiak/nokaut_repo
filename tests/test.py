# -*- coding: UTF-8 -*-

import unittest,urllib2
from mock import patch
from responses import *
from nokaut import lib
from StringIO import StringIO

class NokautExceptionsTest(unittest.TestCase):

    def setUp(self):
        self.nokaut_key = 'a8839b1180ea00fa1cf7c6b74ca01bb5'

    def tearDown(self):
        self.nokaut_key = None

    @patch('nokaut.lib.urllib2')
    def test_success(self, urllib2):
        urllib2.urlopen().return_value = NOKAUT_CORRECT_RESPONSE
        url, price = lib.nokaut_api('rakieta kosmiczna', self.nokaut_key)

    def test_wrong_key_exception(self):
        pass

    def test_no_connection_exception(self):
        pass

    def test_no_key_exception(self):
        pass
