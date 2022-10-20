# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/9/19
# aim: 
from multiprocessing import Queue, Manager, Pool


def test(_a, _b):
    """
    :param _a:
    :param _b:
    :return:
    """
    print(__name__)
    #print(dir(__name__))


class HH(object):
    def __init__(self):
        pass

    def call1(self):
        pass

    def call2(self):
        pass


def main():
    #test(1, 2)
    a = [1, 2, 3, 4]
    print(getattr(test, '_a'))
    # q = Queue.queue
    # m_list = Manager().list()



if __name__ == '__main__':
    main()
