# -*- encoding: utf-8 -*-
"""
@File    :  1811A.py
@Time    :  2023/04/08 08:32:23
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    length, add = [int(_) for _ in input().split()]
    num = input()
    for idx in range(length):
        if add > int(num[idx]):
            return num[:idx] + str(add) + num[idx:]
    return num+ str(add)

t = int(input())
for _ in range(t):
    print(problem())
