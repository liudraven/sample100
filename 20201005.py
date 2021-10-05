# -*-coding : UTF-8 -*-
import os
import sys

class Person(object):
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
