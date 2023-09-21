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

def check_direct(x_center, y_center, x, y):
    if (y==y_center) or (x==x_center):
        return True
    if abs(y-y_center) == abs(x-x_center):
        return True
    return False

for _ in range(int(input())):
    n = int(input().strip())
    points = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if check_direct(*points[i], *points[j]):
                count += 2
    print(count)


