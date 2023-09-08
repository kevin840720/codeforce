# -*- encoding: utf-8 -*-
"""
@File:
    1859B.py
@Time:
    2023/09/01 16:00:54
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1859/B
"""


def problem():
    arrays = []
    n = int(input())
    for _ in range(n):
        array_length = int(input())
        array = [int(_) for _ in input().split()]
        arrays.append(sorted(array))

    first_smallest = [array.pop(0) for array in arrays]
    second_smallest = [array.pop(0) for array in arrays]

    print(sum(second_smallest) - min(second_smallest) + min(min(second_smallest), min(first_smallest)))

t = int(input())
for _ in range(t):
    problem()
