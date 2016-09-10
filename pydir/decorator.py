# -*- coding: utf-8 -*-
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*arg, **kargs):
        print("Enter {func}".format(func=func.__name__))
        return func(*arg, **kargs)
        print("Leave the func ...")
    # return the reference
    return wrapper

def additional(text):
    def log(func):
        # Add this to keep the original information
        #@functools.wraps(func)
        def wrap(*args, **kargs):
            print("%s function:%s" %(text, func.__name__))
            return func(*args, **kargs)
        return wrap
    return log

@additional('Rainy')
def test(text):
    print("Thext input text is %s" %(text)) 

@log
def now():
    import datetime
    print('Current is %s' %(datetime.datetime.now()))

if __name__ == '__main__':
    now()
    test("Wrapper with parameter")
    # Demostrate how to get the wrapping function
    fooo = additional('jj')(test)
    print('function name after wrapper is :' + fooo.__name__)
    fooo('gooog')
