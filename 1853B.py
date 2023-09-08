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

    n = f_{k-1} * a1 + f_{k-2} * a0
    a1 >= a0
"""

def fib2(n):
    if n == 1: return 1, 0
    fn, fn_minus_1 = fib2(n-1)
    return fn + fn_minus_1, fn

def gen_fib(a0, a1, k):
    if k <= 0:
        return []
    return [a0 + a1] + gen_fib(a1, a0+a1, k-1)

def problem():
    n, k = [int(_) for _ in "200000 84".strip().split()]
    c1, c0 = fib2(k-1)

    cand = []
    for i in range(n):
        a0 = i
        a1 = (n - c0*a0)/c1
        if not (a1 >= a0 >= 0):
            break
        if a1 % 1 == 0:
            cand.append((a0, a1))
    
    print(len(cand))
    # for a0, a1 in cand:
    #     ans = [a0, a1] + gen_fib(a0, a1, k-2)
    #     print(" ".join([str(int(_)) for _ in ans]))


# t = int(input())
# for _ in range(t):
#     problem()


# 8
# 22 4
# 3 9
# 55 11
# 42069 6
# 69420 4
# 69 1434
# 1 3
# 1 4