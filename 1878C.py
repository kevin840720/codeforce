# -*- encoding: utf-8 -*-
"""
@File:
    1878C.py
@Time:
    2023/09/26 22:38:48
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1878/problem/C
    .input-template | .py-template.py
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k, x = map(int, input().split())
    upper_bound = (2*n-k+1)*(k//2) if k%2==0 else ((2*n-k+1)//2)*(k)
    lower_bound = (k+1)*(k//2) if k%2==0 else ((k+1)//2)*(k)
    if x > upper_bound or x < lower_bound:
        print("NO")
    else:
        print("YES")

