# -*- coding: utf-8 -*-
class Person(object):
    '''
   Uses class to declare a class
   __slots__ assign a tuple to restrict the 
   instance variable in runtime and define in the class definition
   use @property to declare a getter for prop
   use @propname.setter to declare a setter for prop
   use __doc__ to print document string
    '''
    __slots__ =('name', '_age')
    
    def __init__(self, i_age):
        self._age = i_age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, (int, float)):
            self._age = value
        else:
            raise ValueError('Invalid value:[%s]' %(value,))

    def __str__(self):
        '''just print __doc__ '''
        return Person.__doc__

    __repr__ = __str__


if __name__ == '__main__':
    p = Person(10)
    print('We can assign a new variable to the instance defined in slots:')
    p.name = 'Kate'
    print(p.name)
    p.age = 22
    print('Age of the person is:%s' %(p.age,))
    try:
        p.address = 'Unable to assignment'
    except:
        print('We can not assign address to instance as it is not in predefined slots')

    print(p)
