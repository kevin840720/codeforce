# -*- encoding: utf-8 -*-
"""
@File:
    1883A.py
@Time:
    2023/10/22 19:05:41
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1883/problem/A
    .input-template | .py-template.py
@Status:
    Pretests passed (2)
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    curr = 1
    cost = 4
    for digit in input().strip():
        nxt = 10 if digit == "0" else int(digit)
        cost += abs(nxt - curr)
        curr = nxt
    print(cost)