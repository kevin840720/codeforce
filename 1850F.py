# -*- encoding: utf-8 -*-
"""
@File:
    1850F.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/F
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input().strip())
    frog_counts = [0 for _ in range(n+1)]
    visit_counts = [0 for _ in range(n+1)]
    for frog in map(int, input().split()):
        if frog > n:
            continue
        frog_counts[frog] += 1

    for frog, count in enumerate(frog_counts):
        if frog == 0:
            continue
        for pos in range(frog, n+1):
            if pos%frog==0:
                visit_counts[pos] += count

    print(max(visit_counts))

