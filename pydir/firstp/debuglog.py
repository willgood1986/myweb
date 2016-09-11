# As a log module

from datetime import datetime
global DEBUG
DEBUG = True

def isdebug():
    return DEBUG

def log(content):
    if isdebug():
        print('%s:%s' %(datetime.now(), content))
    
    
