# -*- encoding: utf-8 -*-
"""
@File    :  1791G2.py
@Time    :  2023/04/18 11:51:28
@Author  :  Kevin Wang
@Desc    :  None
"""

from typing import List

def without_initial_position(c, sorted_cost_func):
    n = len(sorted_cost_func)
    idx = 0
    while idx < n and c >= min(sorted_cost_func[idx]):
        c = c - min(sorted_cost_func[idx])
        idx += 1
    return idx

def scenario_1(c, visited:List[tuple]):
    #   1. 計算「如果它當 first step」，我要多付多少錢
    first_step_costs = [x[0]-x[1] for x in visited]
    residue_c = c - sum([_[1] for _ in visited])

    #   2. visited 中，從 cost[1] 大的先 drop，直到 c >= cost of all remained teleports' cost
    possible_count = len(visited) + 1
    while visited:
        cost = visited.pop(-1)
        first_step_cost = first_step_costs.pop(-1)
        residue_c += cost[1]
        possible_count -= 1
        if residue_c >= min(first_step_costs):
            return possible_count
    return -1

def scenario_2(c, visited:List[tuple], unvisited:List[tuple]):
    #   1. 第一步一定是 cost_func[max_possible_count:] 中 cost[0] 最小的那一個
    first_step = min(unvisited, key=lambda x: x[0])
    residue_c = c - sum([_[1] for _ in visited]) - first_step[0]

    #   2. visited 中，從 cost[1] 大的先 drop，直到 c >= cost of all remained teleports' cost
    possible_count = len(visited) + 1
    while visited:
        cost = visited.pop(-1)
        residue_c += cost[1]
        possible_count -= 1
        if residue_c >= 0:
            return possible_count
    return -1

def problem():
    n, c = [int(_) for _ in input().split()]
    a_seq = [int(_) for _ in input().split()]
    cost_func = [(ai+idx+1, ai+n-idx) for idx, ai in enumerate(a_seq)]
    cost_func = sorted(cost_func, key=lambda x: min(x[0], x[1]))

    # if initial position is at 0 or n+1
    max_possible_count = without_initial_position(c, cost_func)
    if max_possible_count == 0:
        return 0
    for cost in cost_func[:max_possible_count]:
        if cost[0] <= cost[1]: # One can be started from position 0
            return max_possible_count

    # All cost[0] < cost[1] for first `max_possible_count` in cost_func
    # 考慮兩種狀況：
    # 1. 第一步已經在 cost_func[:max_possible_count] 中
    # 2. 第一步不在 cost_func[:max_possible_count] 中

    possible_count = [0]
    # Scenario 1：
    possible_count.append(scenario_1(c, cost_func[:max_possible_count]))

    # Scenario 2
    possible_count.append(scenario_2(c, cost_func[:max_possible_count], cost_func[max_possible_count:]))

    return max(possible_count)

t = int(input())
for _ in range(t):
    print(problem())

