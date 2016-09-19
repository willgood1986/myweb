# -*- coding: utf-8 -*-

from os import path as pt

def isapath(i_file):
    ''' use os.path.isdir() to check if the file is a dir
    '''
    return pt.isdir(i_file)

def getabsolutepath(i_file):
    '''
    use os.path.abspath() to retrieve the absolute file name
    '''
    return pt.abspath(i_file)

def getdirectorypart(i_file):
    '''
    use os.path.split()[0] to retrieve the dir part
    '''
    if not isapath(i_file):
        return pt.split(i_file)[0]
    else:
        raise ValueError('{file} is not a file'.format(file=i_file))

def getfilenamepart(i_file):
    '''
    use os.path.split()[1] to rerieve the name part
    '''
    if isapath(i_file):
        raise ValueError('{file} is not a file'.format(file=i_file))
    
    return pt.split(i_file)[1]

def getfileextension(i_file):
    '''
    use os.path.splitext()
    '''
    if isapath(i_file):
        raise ValueError('{file} is not a file'.format(file=i_file))
    
    return pt.splitext(i_file)[1]
