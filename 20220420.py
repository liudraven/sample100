# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/4/20
# aim: 测试父类 ，子类的中的私有属性

class Father(object):
    def __init__(self):
        self.name = 0
        self._age = 1
        self.__id = 2
        pass

    def father_function(self):
        pass

    def __father_function1(self):
        pass

    def _father_function(self):
        print(self.name)
        print(__name__)
        pass

    def father_interface(self):
        pass


class Children(Father):
    def __init__(self):
        super().__init__()

    def children_function(self):
        self.father_function()
        a = self.name
        b = self._age
        c = self.__id
        print(a, b, c)
        pass

    def children_interfacr(self):
        self.__father_function1()
        pass

    def children_interfacr1(self):
        self._father_function()
        pass


def main():
    father = Father()
    a = father._age
    print(a)

    """
    类中的私有变量 __id
    类被实例化了后，不能被实例访问
    不能被子类调用 访问
    
    类的私有方法 __function
    类被实例化后，不能被实例访问
    不能被子类调用
    
    类的保护变量_age
    类被实例化了后，可以被实例访问,  不建议访问
    可以被子类调用 访问
    
    类的保护方法_father_function
    可以被子类调用 访问
    """


def main_1():
    chil = Children()
    chil._father_function()


if __name__ == '__main__':
    main_1()
