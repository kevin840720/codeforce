# -*- encoding: utf-8 -*-
"""
@File:
    1869B.py
@Time:
    2023/09/11 19:03:22
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1869/problem/B
"""

def problem():
    n, k, a, b = [int(_) for _ in input().split()]
    a, b = a-1, b-1
    cities = [[int(_) for _ in input().split()] for _ in range(n)]

    minimum = abs(cities[b][0] - cities[a][0]) + abs(cities[b][1] - cities[a][1])
    dist_a = 2000000001
    dist_b = 2000000001
    for idx in range(k):
        dist_a = min(abs(cities[idx][0] - cities[a][0]) + abs(cities[idx][1] - cities[a][1]), dist_a)
        dist_b = min(abs(cities[idx][0] - cities[b][0]) + abs(cities[idx][1] - cities[b][1]), dist_b)

    print(min(dist_a + dist_b, minimum))

t = int(input())
for _ in range(t):
    problem()