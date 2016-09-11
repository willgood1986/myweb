# -*- coding: utf-8 -*-
class Student(object):
    '''
    A variable starts with __ can not be accessible from
    outsidie, but we can access like instance._ClassName__Pro
    '''
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__name)

if __name__ == '__main__':
    stu = Student("Miss Gao")
    stu.print()
    # access the filed by special name
    print("Access like _Student__name:")
    print(stu._Student__name)
