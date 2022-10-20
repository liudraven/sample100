# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/10/20
# aim:
import time
from multiprocessing.dummy import Pool
import threading


def work(_num):
    time.sleep(1)
    print(threading.current_thread().getName())
    threading.current_thread().setName(_num*_num)
    time.sleep(1)
    print(threading.current_thread().getName())
     # threading.current_thread.__name__ = _num
    time.sleep(1)
    print(_num)


def main():
    pool = Pool(4)
    for i in range(14):
        pool.apply_async(work, (i,))

    pool.close()

    over_list = []
    while True:
        time.sleep(5)
        print("----------------------------------")
        still_count = 0
        for _worker in pool._pool:
            print(_worker.__dict__)
            if _worker._Thread__stopped:
                still_count += 1
        print("still_count:", still_count)

        for _worker in pool._pool:
            print(_worker._Thread__name)
            if _worker._Thread__stopped:
                if _worker._Thread__name not in over_list:
                    print(_worker._Thread__name + "over")
                    over_list.append(_worker._Thread__name)
        if len(over_list) == len(pool._pool):
            break
    print(over_list)
    print('all over')





if __name__ == '__main__':
    main()
