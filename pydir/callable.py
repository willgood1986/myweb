# -*- coding: utf-8 -*-
class TestCall(object):
    '''
    Use callable to test if a function is callable
    override __call__ to make a class callable
    '''
    def __init__(self, name):
        self._name = name


    def __call__(self):
        print('My name is {name}'.format(name = self._name))

    def __str__(self):
        return self.__doc__


if __name__ == '__main__':
    tc = TestCall('Rainy')
    print('We can call the instance directly like tc():')
    tc()
    print('We can use callable to check if the object is callabe like callable(max)')
    print(callable(max))
    print(callable(tc))
    print(None)
    print(tc)
