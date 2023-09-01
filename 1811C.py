# -*- encoding: utf-8 -*-
"""
@File    :  1811C.py
@Time    :  2023/04/08 09:08:35
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    length = int(input())
    b = [int(_) for _ in input().split()]
    a_max = [b[0], b[0]]
    for maximum in b[1:]:
        a_max[-1] = min(a_max[-1], maximum)
        a_max.append(maximum)

    a = [a_max[0]]
    for idx in range(1, length):
        if b[idx-1] != a[-1]:
            a.append(b[idx-1])
        else:
            a.append(a_max[idx])

    return " ".join([str(_) for _ in a])

t = int(input())
for _ in range(t):
    print(problem())
