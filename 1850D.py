# -*- encoding: utf-8 -*-
"""
@File:
    1850D.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/D
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        sorted_ai = sorted(ai)
        splitting = [[sorted_ai[0]]]
        for i in range(n-1):
            if sorted_ai[i+1] - sorted_ai[i] > k:
                splitting.append([sorted_ai[i+1]])
            else:
                splitting[-1].append(sorted_ai[i+1])
        max_len = len(max(splitting, key=len))
        print(n - max_len)

