# -*- coding:UTF-8 -*-

import sys,lib,argparse
from lib import WrongKeyException

parser = argparse.ArgumentParser(description='Nokaut lowest price getter.')
parser.add_argument('-k', help='nokaut personal key')
parser.add_argument('arg')

def parse1_args():
    #function that uses argparse to get user input
    #input: ---
    #output: dictionary
    return vars(parser.parse_args()) #make dict out of Namespace object

def main():
    # function that does the job
    arg, key= parse1_args()['arg'], parse1_args()['k']
    try:
        res = lib.nokaut_api(arg,key)
        print 'Najtańszy przedmiot: ' + res[0] + ' Cena: '+res[1]
    except WrongKeyException:
        sys.exit('Wrong key specified, can\'t get results')


main()
