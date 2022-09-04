# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/8/30
# aim: 
from multiprocessing import Pool
import psutil

def main():
    pool = Pool(100)
    for i in range(100):
        pool.apply_async()
        pool.apply()
        pool.map()
        pool.map_async()

        zip


if __name__ == '__main__':
    main()
