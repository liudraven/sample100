# -*- coding: UTF-8 -*-
import multiprocessing
import time

def sing(n):
    for i in range(n):
        print(i)
        time.sleep(0.1)

def dance(n):
    for i in range(n):
        print(i*i)
        time.sleep(0.1)

if __name__ == '__main__':
    n = 20
    sing_process = multiprocessing.Process(target=sing(n), name='sing')
    dance_process = multiprocessing.Process(target=dance(n))
    sing_process.start()
    dance_process.start()


