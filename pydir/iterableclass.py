# -*- coding: utf-8 -*-
class MyList(object):
    '''
    This demo demonstrates how to make the class iterable
    by overriding __iter__, and __next__ to make the class
    iterable.There are two steps, to override the __iter__
    make the class iterable, to override the __next__ to implement
    the iteration
    '''
    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._index = 0

    def __iter__(self):
        return self
    
    @property
    def isfinished(self):
        return self._index >= self._maxlen

    def __next__(self):
        if not self.isfinished:
            self._index += 1
            return self._index - 1
        else:
            raise StopIteration()

                
if __name__ == '__main__':
    print('Equal to start')
    ml = MyList(10)
    for i in ml:
        print('current is {val}'.format(val = i))
else:
    print('Not Equal')    
