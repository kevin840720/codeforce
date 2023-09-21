# -*- encoding: utf-8 -*-
"""
@File:
    1850G.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/G
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input().strip())
    points = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (points[i][0]==points[j][0]) or (points[i][1]==points[j][1]):
                count += 2
            elif abs(points[j][1]-points[i][1]) == abs(points[j][0]-points[i][0]):
                count += 2
    print(count)


