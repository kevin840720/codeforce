# -*- encoding: utf-8 -*-
"""
@File:
    1853B.py
@Time:
    2023/09/05 21:59:21
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1853/B
"""

def splitting(n):
    if n % 2 == 0:
        m = int(n/2)
        cand = [m+i for i in range(m+1)]
    if n % 2 == 1:
        m = int((n+1)/2)
        cand = [m+i for i in range(m)]
    return cand

def solve_len(aMax, amax):
    if amax >= aMax-amax >= 0:
        return 1 + solve_len(amax, aMax-amax)
    return 2

def bisect(cand):
    a = solve_len(cand[0])
    b = solve_len(cand[-1]) # always 3

N = 18
print(splitting(N))
for i in splitting(N):
    print(i, solve_len(N, i))

# def problem():
#     n, k = [int(_) for _ in input().strip().split()]

# t = int(input())
# for _ in range(t):
#     problem()
