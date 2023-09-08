# -*- encoding: utf-8 -*-
"""
@File:
    1872A.py
@Time:
    2023/09/08 20:25:08
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1872/problem/A
"""
from math import ceil
def problem():
    a, b, c = [int(_) for _ in input().split()]

    print(int(ceil(abs(a-b)/2/c)))

t = int(input())
for _ in range(t):
    problem()
