# -*- coding: UTF-8 -*-
'''计算1-100之间偶数'''


'''def sum_100():
    sum_list = []
    for i in range(1, 101):
        if i % 2 == 0:
            sum_list.append(i)

    return sum_list


content = sum_100()
print(content)'''

'''允许输入3次密码，正确结束，错误继续'''

flag = True


def input_kw():
    global flag

    for i in range(1, 4):
        kw = input('plase input kw:')
        if kw == '32181':
            print('kw right')
            flag = True
            break
        else:
            print('please reinput your kw')
            flag = False

    if not flag:
        print('you have input too many wrong number , please wait a moment ')


input_kw()

