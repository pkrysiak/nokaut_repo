import urllib,urllib2,ast
from lxml import etree

class WrongKeyException(Exception):
    pass

class NoItemException(Exception):
    pass

class NoKeyException(Exception):
    pass

class NoConnectionException(Exception):
    pass

def nokaut_api(p_name, key):
    '''function that takes product name and personal key, searches this phrase in
    nokaut.pl and returns (url, price) of product with the lowest possible price.
    Raises NoKeyException if no key specified, NoConnectionException if no
    internet connection found, and WrongKeyException if wrong key specified.
    input: p_name - string, key - string
    output: tuple (product url - string, price - float)'''

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

    context = etree.fromstring(response.read())

    if context.tag == 'fail':
        raise WrongKeyException('Wrong key, Can\'t get results...')

    url_list = context.xpath('//url//text()')
    min_prices = context.xpath('//price_min//text()')

    if not min_prices:
        raise NoItemException('No items found..')

    url, price = url_list[0].strip(), float(min_prices[0].__str__().replace(',','.'))

    return url, price