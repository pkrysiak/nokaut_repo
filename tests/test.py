# -*- coding: UTF-8 -*-

import unittest,urllib2
from mock import patch,MagicMock
from responses import *
from nokaut import lib
from StringIO import StringIO

class NokautExceptionsTest(unittest.TestCase):

    def setUp(self):
        self.nokaut_key = 'a8839b1180ea00fa1cf7c6b74ca01bb5'

    def tearDown(self):
        self.nokaut_key = None

    @patch('nokaut.lib.urllib2')
    def test_success_1(self, urllib2):
        urllib2.urlopen().read.return_value = NOKAUT_CORRECT_RESPONSE
        url, _ = lib.nokaut_api('rakieta kosmiczna', self.nokaut_key)
        self.assertEqual(url, 'http://www.nokaut.pl/zabawki-kreatywne/zrob-to-sam-rakieta-kosmiczna-4m-3235.html')

    @patch('nokaut.lib.urllib2')
    def test_success_2(self, urllib2):
        urllib2.urlopen().read.return_value = NOKAUT_CORRECT_RESPONSE
        _, price = lib.nokaut_api('rakieta kosmiczna', self.nokaut_key)
        self.assertEqual(price, '29,00')

    @patch('nokaut.lib.urllib2')
    def test_wrong_key_exception(self, urllib2):
        urllib2.urlopen().read.return_value = NOKAUT_WRONG_KEY_RESPONSE
        self.assertRaises(lib.WrongKeyException, lib.nokaut_api, 'rakieta kosmiczna', '1')

    @patch('nokaut.lib.urllib2')
    def test_wrong_phrase_exception(self,  urllib2):
        urllib2.urlopen().read.return_value = NOKAUT_NO_ITEM_RESPONSE
        self.assertRaises(lib.WrongPhraseException, lib.nokaut_api, 'a', self.nokaut_key)

    def test_no_key_exception(self):
        self.assertRaises(lib.NoKeyException, lib.nokaut_api, 'rakieta kosmiczna', '')