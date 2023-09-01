# -*- encoding: utf-8 -*-
"""
@File:
    1753E.py
@Time:
    2023/08/29 11:41:05
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1753/E
"""

import bisect
from dataclasses import dataclass
from math import floor
from typing import List

@dataclass
class Machine:
    operator: str
    number: int

def get_feasible(b, p, m):
    """Solve p*x+m*y <= b for x >= 0, y >= 0
    """
    if b < max(p, m):
        return []

    if p >= m:
        x = floor(b/p)
        y = floor((b-x)/m)
        feasible = [(x, y)]
        for idx in range(1, x+1):
            new_x = int(x-idx)
            new_y = floor((b-new_x)/m)
            feasible.append((new_x, new_y))
    elif p < m:
        y = floor(b/m)
        x = floor((b-y)/p)
        feasible = [(x, y)]
        for idx in range(1, y+1):
            new_y = int(y-idx)
            new_x = floor((b-new_y)/p)
            feasible.append((new_x, new_y))

    return feasible

def problem():
    n, b, p, m = int(input().split(" "))
    feasible = get_feasible(b, p, m)
    max_consider_plus_count = feasible[0][0]
    max_consider_mult_count = feasible[-1][1]

    machines:List[Machine] = []
    multi_machines = []
    plus_machines = []
    for pos in range(n):
        op, num = input().split()
        machines.append(Machine(op, int(num)))
        if op == "+":
            bisect.insort(plus_machines, (int(num), pos), key=lambda x: (x[0], x[1])) 
            plus_machines.append(Machine(op, int(num)))
        elif op == "*":
            multi_machines.append(Machine(op, int(num)))

    prev_plus = []
    while machines[0].operator == "+":
        if machines[0] == plus_machines[-1]:
            prev_plus.append(plus_machines.pop(-1))
            machines = machines[1:]
        else:
            break

    last_mult = []
    while machines[-1].operator == "*":
        if machines[-1] == multi_machines[-1]:
            last_mult.append(multi_machines.pop(-1))
            machines = machines[:-1]
        else:
            break

    


t = int(input())
for _ in range(t):
    print(problem())

feasible = []

