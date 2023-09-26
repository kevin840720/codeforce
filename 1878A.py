# -*- encoding: utf-8 -*-
"""
@File:
    1878A.py
@Time:
    2023/09/26 22:38:48
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1878/problem/A
    .input-template | .py-template.py
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    if k in a:
        print("YES")
    else:
        print("NO")



