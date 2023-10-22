# -*- encoding: utf-8 -*-
"""
@File:
    1877D.py
@Time:
    2023/10/08 18:38:15
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1877/problem/D
    .input-template | .py-template.py
    # REMARK: USE PyPy 3.9 break may lead to RTE
    Related Topic: https://codeforces.com/blog/entry/71276/
"""
R = 998244353
import sys
input = sys.stdin.readline
n = int(input())
an = map(int, input().split())
an_with_idx = sorted(enumerate(an), key=lambda x: -x[1])


factors = [set() for _ in range(n+1)]
for i in range(1, n+1):
    for k in range(i, n+1, i):
        factors[k].add(i)

total = 0
last_i = None
j = n-1
visited_idx = set()
for i, a in an_with_idx:
    total += a*pow(2, j, R)
    if i > 0:
        total += (an_with_idx[i-1][1]-a)*sum(pow(2, d-1, R) for d in factors[last_i+1].difference(visited_idx))
        print("AAA", factors[last_i+1])
        visited_idx = visited_idx.union(factors[last_i+1])
    total %= R
    last_i = i
    j -= 1
    print("visited_idx", visited_idx)
print(total)