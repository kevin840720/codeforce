# -*- encoding: utf-8 -*-
"""
@File:
    1884A.py
@Time:
    2023/10/22 15:08:16
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1884/problem/A
    .input-template | .py-template.py
@Status:
    AC
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x, k = input().strip().split()
    x_i = list(map(int, x))
    x = int(x)
    k = int(k)
 
    gap = k - sum(x_i) % k # UGLY
    if gap == k:
        gap = 0
    elif gap >= 10 - x_i[-1]:
        x += (10 - x_i[-1])
        x_i = list(map(int, str(x)))
        gap = k - sum(x_i) % k
        if gap == k:
            gap = 0
    
    ans = x + gap
    
    print(ans)