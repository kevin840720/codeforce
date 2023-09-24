# -*- encoding: utf-8 -*-
"""
@File:
    1873B.py
@Time:
    2023/09/21 22:38:48
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1873/problem/B
"""
import sys
input = sys.stdin.readline
from functools import reduce
import operator
for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().split()))
    idx = a.index(min(a))
    a[idx] += 1
    print(reduce(operator.mul, a, 1))
    