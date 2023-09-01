# -*- encoding: utf-8 -*-
"""
@File    :  1810D.py
@Time    :  2023/04/10 23:07:16
@Author  :  Kevin Wang
@Desc    :  用 math.ceil 會被 float 搞，導致 TestCase 8 WA
            改用整數除操作
"""
# from math import ceil
# def how_many_days(a, b, h):
#     return max(ceil((h-a)/(a-b) + 1), 1)

def how_many_days(a, b, h):
    q, r = divmod(h-a, a-b)
    n = q + 1 if r == 0 else q + 2
    return max(n, 1)

def rng_intersect(rng1, rng2):
    lb = max(rng1[0], rng2[0])
    ub = min(rng1[1], rng2[1])

    if lb >= ub:
        return None
    return (lb, ub)

def type_1(a, b, n, rng):
    lb = (n-2)*(a-b)+a if n >= 2 else 0
    ub = (n-1)*(a-b)+a
    new_rng = (lb ,ub)
    new_rng = rng_intersect(rng, new_rng)
    if not new_rng:
        return 0, rng
    return 1, new_rng

def type_2(a, b, rng):
    n = how_many_days(a, b, rng[1])
    if n == 1:
        return n
    yesterday_height_max = (n-2)*(a-b)+a
    if yesterday_height_max <= rng[0]:
        return n
    return -1

def problem():
    quest_count = int(input())
    rng = (0, 10**18)
    output = []
    while quest_count > 0:
        quest_count -= 1
        type, *params = [int(_) for _ in input().split()]
        if type == 1:
            a, b, n = params
            resp, rng = type_1(a, b, n, rng)
            output.append(str(resp))
        elif type == 2:
            a, b = params
            h = type_2(a, b, rng)
            output.append(str(h))
    return " ".join(output)

t = int(input())
for _ in range(t):
    print(problem())