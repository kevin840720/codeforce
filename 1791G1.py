# -*- encoding: utf-8 -*-
"""
@File    :  1791G1.py
@Time    :  2023/04/18 11:16:51
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    n, c = [int(_) for _ in input().split()]
    a_seq = [int(_) for _ in input().split()]
    cost_func = [ai+idx+1 for idx, ai in enumerate(a_seq)]
    cost_func = sorted(cost_func)
    idx = 0
    while idx < n and c >= cost_func[idx]:
        c = c - cost_func[idx]
        idx += 1
    return idx

t = int(input())
for _ in range(t):
    print(problem())