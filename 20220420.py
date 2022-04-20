# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/4/20
# aim: 测试父类 ，子类的中的私有属性

class Father(object):
    def __init__(self):
        self.name = 0
        self.__name = 1
        self._age = 2
        pass

    def father_function(self):
        pass

    def __father_function1(self):
        pass

    def _father_function(self):
        pass


class Children(Father):
    def __init__(self):
        super().__init__()

    def chileren_function(self):
        pass

    def


def main():
    pass


if __name__ == '__main__':
    main()
