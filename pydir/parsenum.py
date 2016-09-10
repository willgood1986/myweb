# -*- coding: utf-8 -*-
def Str2Float(i_str):
    from functools import reduce
    ''' use str.slice to a list
        use str.find
        use str[::-1] to revert str
        map(func, range)
        reduce(func(x, y), range)
    '''
    print(Str2Float.__doc__)
    return reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), i_str[:i_str.find('.')])) + reduce(lambda x, y: x / 10.0 + y, map(lambda x: int(x),i_str[i_str.find('.') + 1:][::-1])) / 10.0

def Str2FloatEx(i_str):
    from functools import reduce
    '''s[::-1] reverse a string, :: actually get a sliced string
        when it is left empty, meaning the whole string, -1 means reverse
        s.find('') is a smart guy, when use s[:s.find('')] it returns the 
        left part,
        when we use s[-1:s.find('.'):-1] it returns the right part.
        s.split('.')
        x/y will get the extract result
        x // y will get the int-div result
        USE func.__doc__ to print the doc object in the func
    '''
    print(Str2FloatEx.__doc__)
    #parts = i_str.split('.')
    return reduce(lambda x, y: x * 10 + y, map(int, i_str[:i_str.find('.')])) + reduce(lambda x, y: x / 10 + y, map(int, i_str[-1:i_str.find('.'):-1])) / 10

def TestDoc():
    '''
        This test doc
    '''
    print(TestDoc.__doc__)

if __name__=='__main__':
    print(Str2FloatEx.__doc__)
    result = Str2FloatEx('123.456789')
    print(result)
    TestDoc()
