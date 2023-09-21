# -*- encoding: utf-8 -*-
"""
@File:
    1850G.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/G
"""

import sys
input = sys.stdin.readline
from collections import defaultdict
for _ in range(int(input())):
    n = int(input().strip())
    count = {"x":defaultdict(int),
             "y":defaultdict(int),
             "x+y":defaultdict(int),
             "x-y":defaultdict(int)}
    for i in range(n):
        x, y = map(int, input().split())
        count["x"][x] += 1
        count["y"][y] += 1
        count["x+y"][x+y] += 1
        count["x-y"][x-y] += 1

    total = 0
    for axis in count:
        for v in count[axis].values():
            if v > 1:
                total += v*(v-1)
    print(total)

