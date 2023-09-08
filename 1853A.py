# -*- encoding: utf-8 -*-
"""
@File:
    1853A.py
@Time:
    2023/09/05 21:51:17
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1853/A
"""

def problem():
    n = int(input())
    an = [int(_) for _ in input().split()]

    min_gap = min([x-y for x, y in zip(an[1:], an[:-1])])

    if min_gap < 0:
        print(0)
    else:
        print(int(min_gap/2 + 1))

t = int(input())
for _ in range(t):
    problem()
