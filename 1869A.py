# -*- encoding: utf-8 -*-
"""
@File:
    1869A.py
@Time:
    2023/09/11 18:32:07
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1869/problem/A
"""

def problem():
    n = int(input())
    ai = [int(_) for _ in input().split()]

    act = [(1, n)]
    binary = bin(n)[2:]

    gap = 2**(len(binary)-1)
    act.append((1, gap))
    act.append((n - gap + 1, n))
    act.append((n - gap + 1, n))

    print(len(act))
    for _ in act:
        print(f"{_[0]} {_[1]}")

t = int(input())
for _ in range(t):
    problem()
