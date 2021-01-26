# -*- coding: UTF-8 -*-
'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。 \
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'''
from functools import reduce


'''def actual_a(a, b):
    a = str(a)
    if b == 1:
        return a
    return actual_a(a, b-1)+a


def count_sum(a):
    print('we will count sum of s=a+aa+aaa+aaaa+aa...a', ' please input the Number of calculations ')
    b = int(input('please input '))
    sum_b = 0
    for i in range(1, b+1):
        sum_b += int(actual_a(a, i))
        print(actual_a(a, i))
    return sum_b


output = count_sum(7)
print(output)'''


kk = [1, 2, 3, 4, 5]
#sum_kk = reduce(lambda x, y: x+y, kk)

for x, y in kk:
    sum_kk = lambda x, y: x+y
    print(sum_kk(x,y))

