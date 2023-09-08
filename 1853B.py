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

@Notes:
    n = f(n)*a1 + f(n-1)*a0
"""
from math import ceil, floor
 
def fib2(n):
    if n == 1: return 1, 0
    fn, fn_minus_1 = fib2(n-1)
    return fn + fn_minus_1, fn
 
def ext_euclid(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q = old_r // r
            old_r, r = r, old_r-q*r
            old_s, s = s, old_s-q*s
            old_t, t = t, old_t-q*t
    return old_s, old_t, old_r # old_s*a + old_t*b = gcd(a,b)

def problem():
    n, k = [int(_) for _ in input().strip().split()]
    if k > 27: 
        print(0)
        return
    c1, c0 = fib2(k-1) # c1, c0 must be co-prime
 
    b1, b0, _ = ext_euclid(c1, c0)
    # b1*c1 + b0*c0 = 1

    # Note that
    # n = c1*(b1*n) + c0*(b0*n)
    #   = c1*(b1*n + k*c0) + c0*(b0*n - k*c1) for all k

    # So we take a1, a0
    # a1 = b1*n + k*c0
    # a0 = b0*n - k*c1

    # And by question, we have following constraint
    # w.r.t a1 >= a0 >= 0

    # Therefore, from a0 >= 0, we get k <= b0*n/c1 (note that c1 > 0)
    #            from a1 >= a0, we get k >= (b0-b1)*n/(c1+c0) (note that c1 > 0, c0 >= 0)

    max_k = b0/c1*n
    min_k = (b0-b1)/(c1+c0)*n
    if min_k > max_k:
        print(0)
    else:
        print(floor(max_k) - ceil(min_k) + 1)
 
 
t = int(input())
for _ in range(t):
    problem()