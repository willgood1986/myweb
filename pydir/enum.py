# -*- coding: utf-8 -*-

from enum import Enum

def testenum():
    week = Enum('Week', ('Mon', 'Tues', 'Wes', 'Thu', 'Fri', 'Sat', 'Sun'))
    for name, member in week.__members__.items():
        print('Name:{na}, member:{mem}, value:{val}'.format(na=name, mem=member, val=member.value))


if __name__ == '__main__':
    testenum()
