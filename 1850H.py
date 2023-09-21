# -*- encoding: utf-8 -*-
"""
@File:
    1850H.py
@Time:
    2023/09/21 14:29:44
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/H
"""

import sys
input = sys.stdin.readline
graph = {}
for _ in range(int(input())):
    n, c = map(int, input().split())
    for i in range(c):
        a, b, d = map(int, input().split())
        if a not in graph:
            graph[a] = b
        else:
            graph