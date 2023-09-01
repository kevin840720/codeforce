# -*- encoding: utf-8 -*-
"""
@File    :  1792A.py
@Time    :  2023/02/13 21:12:15
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    count = int(input())
    monsters = [int(_) for _ in input().split()]

    hp1 = len([_ for _ in monsters if _ == 1])
    hp2 = len(monsters) - hp1
    return (hp1+1)//2 + hp2


t = int(input())
for _ in range(t):
    print(problem())

