# -*- encoding: utf-8 -*-
"""
@File:
    1859C.py
@Time:
    2023/09/02 08:47:23
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1859/C
    # REMARK: 需要證明
"""

def square_sum(n):
    return (n*(n+1)*(2*n+1))/6

def conv_sum(n, i):
    return (n+i)*(n+i)*(n-i+1)/2 - square_sum(n) + square_sum(i-1)

def max_one(n, i):
    if n == i:
        return n**2
    a = (n+i)/2
    if a%1==0:
        return a**2
    return int(a)*(int(a)+1)

def problem():
    n = int(input())
    cand = [square_sum(i) + conv_sum(n, i+1) - max_one(n,i+1) for i in range(n)]
    print(int(max(cand)))
        

t = int(input())
for _ in range(t):
    problem()
