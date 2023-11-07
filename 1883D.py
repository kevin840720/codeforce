# -*- encoding: utf-8 -*-
"""
@File:
    1883D.py
@Time:
    2023/10/22 20:25:01
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1883/problem/D
    1883D.input | 1883D.py
@Status:
    Time limit exceeded on pretest 4
"""
from time import time
a = time()
import sys
input = sys.stdin.readline

l_dict = {-1:-1}
r_dict = {10**9+1:-1}
min_r, max_l = 10**9+1, -1
count = 0
for _ in range(int(input())):
    op, l, r = input().split()
    l, r = int(l), int(r)
    if op == "+":
        if l not in l_dict:
            l_dict[l] = 0
        if r not in r_dict:
            r_dict[r] = 0
        l_dict[l] += 1
        r_dict[r] += 1
        min_r = min(min_r, r)
        max_l = max(max_l, l)
        count += 1
    else:
        l_dict[l] -= 1
        r_dict[r] -= 1
        if l_dict[l] == 0:
            l_dict.pop(l)
            max_l = max(l_dict)
        if r_dict[r] == 0:
            r_dict.pop(r)
            min_r = min(r_dict)
        count -= 1

    # if count <= 1:
    #     print("NO")
    # else:
    #     if min_r < max_l:
    #         print("YES")
    #     else:
    #         print("NO")



b = time()
print(b-a)