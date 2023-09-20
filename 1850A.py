# -*- encoding: utf-8 -*-
"""
@File:
    1850A.py
@Time:
    2023/09/19 21:30:33
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/A
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a+b>=10 or b+c>=10 or a+c>=10:
        print("YES")
    else:
        print("NO")