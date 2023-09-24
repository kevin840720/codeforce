# -*- encoding: utf-8 -*-
"""
@File:
    1873C.py
@Time:
    2023/09/21 22:42:54
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1873/problem/C
"""
import sys
input = sys.stdin.readline
f = lambda x, y: max(abs(x-4.5), abs(y-4.5))
for _ in range(int(input())):
    score = 0
    for col in range(10):
        a = input().strip()
        rows = [row for row in range(10) if a[row] == "X"]
        for row in rows:
            if f(col, row):
                score += int(5.5 - f(col, row))
    print(score)
            