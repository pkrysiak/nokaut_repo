import urllib
from lxml import etree
from StringIO import StringIO
from types import StringType


class WrongKeyException(Exception):
        '''
                class which handles input error excepton
        '''
        def __str__(self):
                return repr("Wrong key, Can't get results...")

def nokaut_api(p_name, key):
    if not isinstance(key, StringType):
        raise TypeError
    question = 'http://api.nokaut.pl/?format=xml&key='+key+'&method=nokaut.product.getByKeyword&keyword='+p_name
    response = urllib.URLopener().open(question)
    xml = response.read()
    context = etree.parse(StringIO(xml))
    product_list = context.xpath('//name//text()')
    min_prices = context.xpath('//price_min//text()')
    # print (product_list,min_prices)
    if not product_list:
        raise WrongKeyException
    return (product_list[0],min_prices[0])


# print nokaut_api('3310', 'a8839b1180ea00fa1cf7c6b74ca01bb5')
# print nokaut_api('3310', '12')