# -*- coding: utf-8 -*-
from math import sqrt

def parse_x_from_equation(a, b, c):
    ''' ax^2+bx+c=0'''
    # check parameters
    if not isinstance(a, (int,float)):
        raise TypeError('{a} is not an int or float type'.format(a=a))
    if not isinstance(b, (int, float)):
        raise TypeError('{b} is not an int or float type'.format(b=b))
    if not isinstance(c, (int, float)):
        raise TypeError('{c} is not an int or float type'.format(c=c))
    
    delt = b**2 - 4*a*c
    if delt>= 0:
        x1 = (-b + sqrt(delt))/(2*a)
        x2 = (-b - sqrt(delt))/(2*a)
        return x1, x2
    else:
        print('there is no answer due to input {a}, {b}, {c}'.format(a=a, b=b, c=c))


if "__main__" == __name__:
    results = parse_x_from_equation(2, 9, 7)
    print(results)
        
    
    
