# -*- coding:UTF-8 -*-
# auther:drliu
# aim: 装饰器
import time


def log_decorater(fuc):
    """
    aim to build more features for input function
    :param fuc: raw function
    :return: new function
    """
    def decorator(*args, **kwargs):
        print('INFO::', 'will do function:{0}'.format(fuc.__name__))
        a = time.perf_counter()
        print('INFO::', 'function:{0} begin time:{1}'.format(fuc.__name__, time.strftime('%Y-%m-%d %H:%M:%S')))

        ret = fuc(*args, **kwargs)

        print('INFO::', 'function:{0} completed'.format(fuc.__name__))
        b = time.perf_counter()
        print('INFO::', 'function:{0} end time:{1}'.format(fuc.__name__, time.strftime('%Y-%m-%d %H:%M:%S')))
        cost_time = b - a
        print('INFO::', 'function:{0} cost time:{1} s'.format(fuc.__name__, cost_time))

        return ret
    return decorator


@log_decorater
def main(num=1):
    time.sleep(3)
    return num


if __name__ == '__main__':
    print(main())


