# -*- coding: UTF-8 -*-
'''判断101-200之间有多少个素数，并输出所有素数。'''



def ct(a, b):
    global s_number
    s_number = []
    for i in range(a, b):
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                s_number.append(i)
                continue

    all_number = set(range(101, 201))
    s_number = set(s_number)
    final_number = list(all_number ^ s_number)

    print(final_number)
    print(len(final_number))


if __name__ == '__main__':
    ct(101, 201)





