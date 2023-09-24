# -*- encoding: utf-8 -*-
"""
@File:
    1873D.py
@Time:
    2023/09/21 22:42:54
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1873/problem/D
"""
# type 1873D-pressure.txt | python 1873D.py
from time import time

import sys
input = sys.stdin.readline
import re
for _ in range(int(input())):
    n, k = map(int, input().split())
    cells = input().strip().strip("W")
    cells += "W"*k
    count = 0
    aa = re.findall(f"B[WB]{{{k-1},{k-1}}}", cells)
    count = len(aa)
    print(count)


# from time import time

# import sys
# input = sys.stdin.readline
# import re
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     cells = input().strip().strip("W")
#     rev = cells[::-1]
#     a = time()
#     count = 0
#     for regex in re.split(f"W{{{k-1},}}", cells):
#         count += len(regex)//k + (len(regex)%k!=0)
        
        
#     b = time()
#     print("AAAAAAAAA", count)

#     print(b-a)