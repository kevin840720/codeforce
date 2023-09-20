# -*- encoding: utf-8 -*-
"""
@File:
    1850B.py
@Time:
    2023/09/19 21:30:33
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/B
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = 1
    maximum = -1
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > maximum:
            maximum = b
            ans = i+1
    print(ans)