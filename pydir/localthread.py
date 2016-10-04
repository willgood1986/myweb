# -*- coding: utf-8 -*-
import threading

thrdvar = threading.local()

def process():
    name = thrdvar.name
    print('hello % r in thread %r' %(name, threading.current_thread().name))

def run(name):
    thrdvar.name = name
    process()

if __name__ == '__main__':
    t = threading.Thread(target=run, args=('jim',), name='jim thread')
    t1 = threading.Thread(target=run, args=('tom',), name='tom thread')
    t.start()
    t1.start()
    t.join()
    t1.join()
    print('The main thread is over...')
