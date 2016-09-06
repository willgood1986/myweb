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

if __name__=='__main__':
    result = Str2Float('123.456')
    print(result)
