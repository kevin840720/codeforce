# -*- encoding: utf-8 -*-
"""
@File    :  1810A.py
@Time    :  2023/04/10 16:15:10
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    n = int(input())
    an = [int(_) for _ in input().split()]

    count = 0
    for a in an:
        count += 1
        if a <= count:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    print(problem())
