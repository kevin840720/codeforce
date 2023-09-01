# -*- encoding: utf-8 -*-
"""
@File    :  1814C.py
@Time    :  2023/04/13 16:37:55
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    n, s1, s2 = [int(_) for _ in input().split()]
    required = [int(_) for _ in input().split()]
    workload = n*s2//(s1 + s2) # ideal workload ratio of robot 1: s2/(s1 + s2)

    box_order = sorted(range(1, n+1), key=lambda x:required[x-1], reverse=True)

    robot1 = []
    robot2 = []
    timer1 = s1
    timer2 = s2
    for box in box_order:
        if timer1 < timer2:
            robot1.append(box)
            timer1 += s1
        else:
            robot2.append(box)
            timer2 += s2
    print(" ".join([str(_) for _ in [len(robot1)] + robot1]))
    print(" ".join([str(_) for _ in [len(robot2)] + robot2]))

t = int(input())
for _ in range(t):
    problem()
