# -*- coding: utf-8 -*-
class MyItems(object):
    '''
    We can simulate the obj[index] by __getitem__
    slice type, start, stop
    __init__: constructor
    __iter__: IEnumerable
    __next__: GetIteration
    '''
    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._index = 0


    def __iter__(self):
        return self

    def _isover(self):
        return self._index >= self._maxlen

    def __next__(self):
        if not self._isover():
            self._index += 1
            return self._index
        else:
            raise StopIteration()

    def __getitem__(self, n):
        if isinstance(n, int):
            if n < self._maxlen:
                return n + 1
            else:
                raise ValueError('Out of range')
            return n
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            if (stop is None) or (stop > self._maxlen):
                stop = self._maxlen
            return list(range(1, self._maxlen))[start:stop]

    def __str__(self):
        return self.__doc__

    __repr__ = __str__

if __name__ == '__main__':
    mi = MyItems(10)
    for i in mi:
        print('for in, current is {val}'.format(val = i))

    print('get item by index')
    print(mi[2])
    print('Slice 1:3')
    x = mi[2: 20]

if __name__ == '__main__':
    mi = MyItems(10)
    print('Item at 5:%d'%( mi[5],))

    print('slice 4: 8')
    sliced = mi[4:8]
    for i in sliced:
        print('sliced current value is {val}'.format(val = i)) 

    print(mi)  
