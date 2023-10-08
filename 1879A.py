# -*- encoding: utf-8 -*-
"""
@File:
    1879A.py
@Time:
    2023/09/24 17:49:27
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1879/A
    .input-template | .py-template.py
    # REMARK: USE PyPy 3.9 break may lead to RTE
    Related Topic: https://codeforces.com/blog/entry/71276/
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s1, e1 = map(int, input().split())
    w = s1
    for i in range(n-1):
        si, ei = map(int, input().split())
        if si >= s1 and ei >= e1:
            w = -1
    print(w)

