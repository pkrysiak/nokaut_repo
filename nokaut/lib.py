import urllib
from lxml import etree


class WrongKeyException(Exception):

        def __init__(self,str):
            self.str = str

        def __str__(self):
                return repr(self.str)

class NoKeyException(Exception):
    pass

class NoConnectionException(Exception):
    pass


def nokaut_api(p_name, key):
    question = 'http://api.nokaut.pl/?format=xml&key='+key+'&method=nokaut.product.getByKeyword&keyword='+p_name
    response = urllib.URLopener().open(question)
    context = etree.parse(response)
    product_list = context.xpath('//name//text()')
    min_prices = context.xpath('//price_min//text()')
    # print (product_list,min_prices)
    if not product_list:
        raise WrongKeyException('Wrong key, Can\'t get results...')
    return product_list[0], min_prices[0]


# print nokaut_api('3310', 'a8839b1180ea00fa1cf7c6b74ca01bb5')
# print nokaut_api('3310', '12')