# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/2/26
# aim: 装饰器函数名，函数执行时间

import time
from print_log import print_log


def function_info(original_fuction):
    """
    无配置，有包装
    :return:
    """
    def decorator_fuction(*args, **kwargs):
        function_name = original_fuction.__name__
        print_log('INFO', 'function:{0} start '.format(function_name))
        start_time = time.time()
        result = original_fuction(*args, **kwargs)
        end_time = time.time()
        exe_time = end_time - start_time
        print_log('INFO', 'function:{0} end '.format(function_name))
        print_log('INFO', 'function:{0} exe time is {1}(s)'.format(original_fuction.__name__, exe_time))
        return result

    return decorator_fuction


def decoration_sample_step_0(decorator_fuction):
    """
    无入参，无包装
    :return:
    """
    def do_something(_fuction):
        print_log('DEBUG', 'now executing function is :{0}'.format(_fuction.__name__))
        setattr(_fuction, 'function_type', 'sample')
        print_log('DEBUG', 'now executing function type is :{0}'.format(_fuction.function_type))
        pass
    do_something(decorator_fuction)

    return decorator_fuction


def decoration_sample_step_1(original_function):
    """
    无入参，有包装
    :return:
    """
    def decorator_fuction():
        start_time = time.time()
        result = original_function()
        end_time = time.time()
        exe_time = end_time - start_time
        print_log('DEBUG', 'function {0} exe_time is {1}(s)'.format(original_function.__name__, exe_time))
        return result

    return decorator_fuction


def decoration_sample_step_2(original_function):
    """
    有函数入参，无装饰器入参，无包装
    :return:
    """

    def decorator_fuction(*args, **kwargs):
        result = original_function(*args, **kwargs)
        print_log('INFO', '有函数入参，无装饰器入参，无包装')
    return decorator_fuction


def decoration_sample_step_3(input_parameter):
    """
    有装饰器入参，有函数入参
    :return:
    """
    def decorator_fuction_1(func):

        def decorator_fuction_2(*args, **kwargs):
            if input_parameter == 1:
                print("----权限级别1，验证----")
            elif input_parameter == 2:
                print("----权限级别2，验证----")
            return func(*args, **kwargs)

        return decorator_fuction_2

    return decorator_fuction_1


def set_level(level_num):
    """有装饰器入参，有函数入参，无包装"""
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("----权限级别1，验证----")
            elif level_num == 2:
                print("----权限级别2，验证----")
            return func(*args, **kwargs)
        return call_func
    return set_func


@decoration_sample_step_3(2)
def test_original(a):
    """测试函数"""
    print_log('INFO', a)
    print_log('INFO', 'this is only one test original function')
    return 'success', 'hello world'


def main():
    result = test_original('wow')
    print_log('INFO', 'result is {0}'.format(result))


if __name__ == '__main__':
    main()
