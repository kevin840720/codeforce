# -*- encoding: utf-8 -*-
"""
@File:
    1873D.py
@Time:
    2023/09/21 22:42:54
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1873/problem/D
"""
# type 1873D-pressure.txt | python 1873D.py
from time import time

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    cells = input().strip()
    a = time()
    count = 0
    idx = cells.find("B")
    if idx == -1:
        idx = len(cells)
    while idx < len(cells):
        idx += k
        count += 1
        nxt = cells[idx:].find("B")
        if nxt == -1:
            break
        idx += nxt
        
    b = time()
    print("AAAAAAAAA", count)

    print(b-a)