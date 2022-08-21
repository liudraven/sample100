# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/8/10
# aim: practise re module
import os.path
import re
import sys
sys.setprofile(tracefunc)

def main():
    #sample_str = 'ahhh就阿萨123，121121,asad12阿达123123'
    sample_str = '1212'
    sample_compare = re.compile(r'\d')
    result = sample_compare.findall(sample_str)
    result2 = sample_compare.match(sample_str)
    print(result)
    print(result2)
    print(re.match(r'\d', sample_str).groups())


if __name__ == '__main__':
    main()
    print(__file__)
    print(os.path.abspath(__file__))
    sys.stdout.flush()