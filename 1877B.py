# -*- encoding: utf-8 -*-
"""
@File:
    1877B.py
@Time:
    2023/10/08 17:09:58
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1877/problem/A
    .input-template | .py-template.py
    # REMARK: USE PyPy 3.9 break may lead to RTE
    Related Topic: https://codeforces.com/blog/entry/71276/
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, p = map(int, input().split())
    a_seq = map(int, input().split())
    b_seq = map(int, input().split())
    announced = 1
    cost = p
    for b, a in sorted(zip(b_seq, a_seq)):
        if b < p:
            if announced + a <= n:
                announced += a
                cost += a*b
            elif announced + a > n:
                cost += (n-announced)*b
                announced = n
                break
        else:
            cost += (n-announced)*p
            break
    print(cost)
    
