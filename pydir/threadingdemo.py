# -*- coding: utf-8 -*-
import threading, time
def loops():
    print('run 20 rounds ...')
    
    round = 1
    while round < 20:
        print('round %r' % round)
        time.sleep(5)
        round += 1

def runthread():
    t = threading.Thread(target=loops, name='loops')
    t.start()
    t.join()
    print('Thread is over~')


if __name__ == '__main__':
    runthread()
        
