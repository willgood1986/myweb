# -*- coding: utf-8 -*-
class GetAttr(object):
    ''' When a property is not found in the class,
    it goes to class definition to query from __getattr__
    when we want to give an handle on some known attrs, we
    can override the __getattr__, this also applies to slots
    '''
    __slots__ = ('age',)
    def __init__(self):
        pass

    def __getattr__(self, attr):
        if attr == 'name':
            return 'Unknown name'

    def __str__(self):
        return self.__doc__

    __repr__ = __str__


if __name__ == '__main__':
    ga = GetAttr()
    print(ga.name)
    print(ga)
   
