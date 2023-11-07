# -*- encoding: utf-8 -*-
"""
@File:
    1883B.py
@Time:
    2023/10/22 19:12:13
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1883/problem/B
    .input-template | .py-template.py
@Status:
    Pretests passed (4)
"""
from collections import Counter
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    counter = Counter(s)
    oddcount = len([k for k, v in counter.items() if v%2 != 0])
    mincost = oddcount - 1
    if mincost == k:
        print("YES")
    elif mincost > k:
        print("NO")
    else:
        print("YES")
