# -*- coding: utf-8 -*-

def testprocessid():
     import os
     
     print('This is a testing process: %r' % os.getpid())
     
     pid =os.fork()
     if pid == 0:
         print('Child:%r, parent id:%r' %(os.getpid(), os.getppid()))
     else:
         print('Create a child process %r' % pid)
    
    
if __name__ == '__main__':
    testprocessid()     
     


