# -*- encoding: utf-8 -*-
"""
@File:
    1850E.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/E
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, c = map(int, input().split())
    paints = list(map(int, input().split()))

    square_sum = sum(map(lambda x: pow(x,2), paints.copy()))
    summation = sum(paints)

    ans = (round(pow(summation**2 - n*(square_sum-c), 0.5)) - summation)/(2*n)
    print(round(ans))

