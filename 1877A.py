# -*- encoding: utf-8 -*-
"""
@File:
    1877A.py
@Time:
    2023/10/08 17:07:43
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
    n = int(input())
    a = sum(map(int, input().split()))
    print(-a)

