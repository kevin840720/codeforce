# -*- encoding: utf-8 -*-
"""
@File:
    1884C.py
@Time:
    2023/10/22 15:56:40
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1884/problem/C
    .input-template | .py-template.py
@Status:
    Uncommit
"""
from itertools import accumulate
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    for _ in range(m):
        l, r = map(lambda x: int(x) - 1, input().split())
        left[l] += 1
        right[r] += 1
    height = list(accumulate([l-r for l, r in zip(left, right)]))

        



