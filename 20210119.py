# -*- coding: UTF-8 -*-
'''打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方'''
import math


count_list = []


def shui_count():
    global count_list
    for i in range(100, 1000):
        for a in range(0, 10):
            for b in range(0, 10):
                for c in range(0, 10):
                    m = a ** 3 + b ** 3 + c ** 3
                    if m == i and i == 100*a + 10*b + c:
                        count_list.append(m)
                        print(m)
    return count_list


'''def shui_count():
    global count_list
    for m in range(100, 1000):
        a = math.floor(m/100)
        b = math.floor((m - 100*a)/10)
        c = m - 100*a - 10*b
        print(a, b, c)
        if m == (a**3 + b**3 + c**3):
            count_list.append(m)
            print(m)
    return count_list'''


shui= shui_count()

print(shui)





