# -*- coding:UTF-8 -*-

import getopt,sys,lib
from lib import WrongKeyException


def parse_args():
    key = False
    args = sys.argv[1:]
    try:
        optlist, arg = getopt.getopt(args,'k:')
        # print optlist,arg

        if not arg:
            sys.exit('No search argument specified...')
        elif len(arg) > 1:
            sys.exit('To many arguments specified...')

        for option,argument in optlist:
            if option == '-k':
                key = argument

        if not key:
            sys.exit('No key specified..')

        return (arg[0],key)

    except getopt.GetoptError:
        sys.exit(' wrong inpunt, example input: \n scripts.py -k [key] [product name]')


def main():
    arg,key= parse_args()
    try:
        res = lib.nokaut_api(arg,key)
        print 'Najtańszy przedmiot: '+res[0]+' Cena: '+res[1]
    except WrongKeyException:
        sys.exit('Wrong key specified, can\'t get results')
main()