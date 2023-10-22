# -*- encoding: utf-8 -*-
"""
@File:
    1877C.py
@Time:
    2023/10/08 17:22:04
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1877/problem/A
    .input-template | .py-template.py
    # REMARK: USE PyPy 3.9 break may lead to RTE
    Related Topic: https://codeforces.com/blog/entry/71276/
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if m < n:
        if k == 1:
            print(1)
        elif k == 2:
            print(m)
        else:
            print(0)
    elif m >= n:
        if k == 1:
            print(1)
        elif k == 2:
            print(n-1 + m//n)
        elif k == 3:
            print(m - n + 1 - m//n)
        else:
            print(0)
