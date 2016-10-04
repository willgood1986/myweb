# -*- coding: utf-8 -*-
import threading, time
balance = 0

lock = threading.Lock()

def change(n):
    global balance
    lock.acquire()
    try:
        balance += n
        balance -= n
    finally:
        lock.release()

def run(n):
    for i in range(100000):
        if i == 999:
            print('go to 9999')
        change(n)
        if (i / 100 == 0):
            print('balance %r' % balance)

def twothrds():
    t1 = threading.Thread(target=run, args=(5,), name='first(5)')
    t2 = threading.Thread(target=run, args=(8,), name='second(8)')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('All is over ...')

if __name__ == '__main__':
    twothrds()
