# -*-coding : UTF-8 -*-
import os
import sys

class Person(object):
    '''
    经典类中只能关联读取方法
    只有在新式类中才能关联设置方法
    '''
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def return_init(self):
        print(self.__age)

p = Person()
p.age = 200
print(p.age)
