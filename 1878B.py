# -*- encoding: utf-8 -*-
"""
@File:
    1878B.py
@Time:
    2023/09/26 22:38:48
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1878/problem/B
    .input-template | .py-template.py
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input().strip())
    print(" ".join([str(3*k + 1) for k in range(4, n+4)]))
