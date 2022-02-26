# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/2/25
# aim: 装饰器模式
def decorator_fuc2(origin_func):
    '''
    希望对函数进行加工
    :param origin_func:
    :return:
    '''
    def decorator_fuc(*args, **kwargs):
        a = origin_func(*args, **kwargs)
        return a

    return decorator_fuc


@decorator_fuc2
def fuc1(sample):
    print('sample:%s' % sample)
    print('hello')
    return 'hello', 'require'


def decorator_fuc1(origin_func):
    '''
    每次使用都要对函数进行加工，而不是一次性加工结束
    :param origin_func:
    :return:
    '''
    #a = origin_func()
    #return a
    a = origin_func()
    return a


def main():
    # print('origin_fuc')
    # a = fuc1()
    # print(a)
    # print('decorator_fuc')
    # b = decorator_fuc1(fuc1)
    # print(b)
    print('decorator_fuc')
    #fuc2 = decorator_fuc2(fuc1)
    a = fuc1('hhaa')
    print(a)


if __name__ == '__main__':
    main()
