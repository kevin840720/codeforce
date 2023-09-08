# -*- encoding: utf-8 -*-
"""
@File:
    1872B.py
@Time:
    2023/09/08 18:59:32
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1872/problem/B
"""

from math import floor
def problem():
    n = int(input())
    trap = {}
    for _ in range(n):
        di, si = [int(_) for _ in input().split()]
        trap[di] = si if di not in trap else min(si, trap[di])

    nearest = 1000
    for di, si in trap.items():
        nearest = min(nearest, di + floor((si-1)/2))
    print(nearest)

t = int(input())
for _ in range(t):
    problem()
