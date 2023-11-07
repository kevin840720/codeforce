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
    Uncommit
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    inv = s[::-1]
    last_row = [0 for _ in range(n+1)]
    curr_row = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(n+1):
            if j == 0:
                curr_row[j] = i
            elif s[j-1] == inv[i-1]:
                curr_row[j] = last_row[j-1]
            else:
                curr_row[j] = last_row[j]+1
        last_row = curr_row.copy()
    mincost = min(last_row)
    if mincost == k:
        print("YES")
    elif mincost > k:
        print("NO")
    elif mincost < k and n%2 == k%2:
        print("YES")
    else:
        print("NO")

    