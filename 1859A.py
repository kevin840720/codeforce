# -*- encoding: utf-8 -*-
"""
@File:
    1859A.py
@Time:
    2023/09/01 14:34:55
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1859/A
"""

def problem():
    n = int(input())
    an = [int(_) for _ in input().split()]

    elem = min(an)
    bn = [str(elem)]*an.count(elem)
    cn = [str(_) for _ in an if _ != elem]

    if len(cn) >= 1:
        print(len(bn), len(cn))
        print(' '.join(bn))
        print(' '.join(cn))
    else:
        print("-1")


t = int(input())
for _ in range(t):
    problem()
