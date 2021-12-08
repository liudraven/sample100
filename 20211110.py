# -*- coding:UTF-8 -*-
# auther:drliu
# aim: 

def main(a, *args, **kwargs):
    print(a)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(key, value)


if __name__ == '__main__':
    main('a', 'a', 'b', read_flag=1, read_num=2)
