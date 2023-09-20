# -*- encoding: utf-8 -*-
"""
@File:
    1867A.py
@Time:
    2023/09/12 17:04:01
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1867/A
"""

for I in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    ai_order = sorted(range(n), key=lambda i: ai[i])
    bi = [None]*n
    for j, i in enumerate(ai_order):
        bi[i] = str(n - j)
    print(" ".join(map(str, bi)))
