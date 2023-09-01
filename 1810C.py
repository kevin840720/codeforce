# -*- encoding: utf-8 -*-
"""
@File    :  1810C.py
@Time    :  2023/04/10 17:00:48
@Author  :  Kevin Wang
@Desc    :  None
"""

def start_from_1(n, del_cost, ins_cost, seq, seq_set, maximum):
    insertion_init_count = 0
    deletion_init_count = n

    curr = deletion_init_count*del_cost + insertion_init_count*ins_cost # 這個是全 delete，不記入答案
    best = -1
    for i in range(1, maximum+1):
        if i not in seq_set:
            curr += ins_cost
        elif i in seq_set:
            curr -= del_cost
        best = min(curr, best) if best >= 0 else curr
    return best

def start_from_n(n, del_cost, ins_cost, seq, seq_set, maximum):
    insertion_init_count = maximum - len(seq_set)
    deletion_init_count = len(seq) - len(seq_set)

    curr = deletion_init_count*del_cost + insertion_init_count*ins_cost # 這個是全 insert，記入答案
    best = curr
    for i in range(maximum, 0, -1):
        if i not in seq_set:
            curr -= ins_cost
        elif i in seq_set:
            curr += del_cost
        best = min(curr, best) if best >= 0 else curr
    return best

def problem():
    n, del_cost, ins_cost = [int(_) for _ in input().split()]
    seq = [int(_) for _ in input().split()]
    seq_set = set(seq)
    maximum = max(n, max(seq_set))

    return start_from_1(n, del_cost, ins_cost, seq, seq_set, maximum)
    return start_from_n(n, del_cost, ins_cost, seq, seq_set, maximum)


t = int(input())
for _ in range(t):
    print(problem())
