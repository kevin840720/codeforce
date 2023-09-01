# -*- encoding: utf-8 -*-
"""
@File    :  1810B.py
@Time    :  2023/04/10 16:22:53
@Author  :  Kevin Wang
@Desc    :  None
"""

def inv_f1(x):return (x + 1)/2
def inv_f2(x):return (x - 1)/2
def problem():
    n = int(input())
    action = []
    if n % 2 == 0:
        return -1
    count = 0
    while n > 1:
        next = inv_f1(n)
        if next % 2 == 0:
            next = inv_f2(n)
            action = ["2"] + action
        else:
            action = ["1"] + action
        n = next
        count += 1
    print(count)
    return " ".join(action)

t = int(input())
for _ in range(t):
    print(problem())
