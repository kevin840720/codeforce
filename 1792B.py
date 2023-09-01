# -*- encoding: utf-8 -*-
"""
@File    :  1792B.py
@Time    :  2023/02/13 21:20:40
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    jokes = [int(_) for _ in input().split()]
    if jokes[0] == 0:
        return 1

    mood = [jokes[0], jokes[0]]
    count = jokes[0]
    jokes[0] = 0
    if jokes[1] > jokes[2]:
        tmp = jokes[2]
        jokes[2] = jokes[1]
        jokes[1] = tmp

    count += jokes[1]*2
    jokes[2] -= jokes[1]
    jokes[1] = 0

    if mood[0] - jokes[2] >= 0:
        count += jokes[2]
        mood[0] -= jokes[2]
    else:
        return count + mood[0] + 1

    return count + min(min(mood)+1, jokes[3])

t = int(input())
for _ in range(t):
    print(problem())
