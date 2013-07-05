import urllib,urllib2
from lxml import etree


class WrongKeyException(Exception):

    def __init__(self,msg=''):
        self.msg = msg

    def __str__(self):
            return repr(self.str)

class NoKeyException(Exception):

    def __init__(self,msg=''):
            self.msg = msg

    def __str__(self):
           return repr(self.msg)

class NoConnectionException(Exception):

    def __init__(self,msg=''):
        self.msg = msg

    def __str__(self):
            return repr(self.msg)

def nokaut_api(p_name, key):
    '''function that takes product name and personal key, searches this phrase in
    nokaut.pl and returns (url, price) of product with the lowest possible price.
    Raises NoKeyException if no key specified, NoConnectionException if no
    internet connection found, and WrongKeyException if wrong key specified.
    input: p_name - string, key - string
    output: tuple (product url - string, price - string)'''

    if key == '':
        raise NoKeyException('No key specified.')

    url = 'http://api.nokaut.pl/'
    url_data = {'keyword' : p_name,
                'method' : 'nokaut.product.getByKeyword',
                'key' : key,
                'format' : 'xml'}

    data = urllib.urlencode(url_data)
    question = '?'.join([url,data])

    try:
        response = urllib2.urlopen(question)
    except IOError:
        raise NoConnectionException('No internet connection.')

    context = etree.parse(response)
    url_list = context.xpath('//url//text()')
    min_prices = context.xpath('//price_min//text()')

    if not url_list:
        raise WrongKeyException('Wrong key, Can\'t get results...')

    return url_list[0], min_prices[0]

# print nokaut_api('3310', 'a8839b1180ea00fa1cf7c6b74ca01bb5')