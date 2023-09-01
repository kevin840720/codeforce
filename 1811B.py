# -*- encoding: utf-8 -*-
"""
@File    :  1811B.py
@Time    :  2023/04/08 08:49:49
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    n, x1, y1, x2, y2 = [int(_) for _ in input().split()]
    half_len = int(n/2) + 0.5
    new_x1 = x1 - half_len
    new_y1 = y1 - half_len
    new_x2 = x2 - half_len
    new_y2 = y2 - half_len

    ribbon1 = max(abs(new_x1), abs(new_y1))
    ribbon2 = max(abs(new_x2), abs(new_y2))

    return int(abs(ribbon2 - ribbon1))

t = int(input())
for _ in range(t):
    print(problem())
