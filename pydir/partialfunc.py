# -*- coding: utf-8 -*-
''' Us partial to wrap and return a new function with default parameters
'''
from functools import partial
int2 = partial(int, base=2)

if __name__ == '__main__':
    print('%s' %(int2('1010011')))

