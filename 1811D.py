# -*- encoding: utf-8 -*-
"""
@File    :  1811D.py
@Time    :  2023/04/09 08:07:28
@Author  :  Kevin Wang
@Desc    :  None
"""

def problem():
    n, i, j = [int(_) for _ in input().split()]
    fp, fn = 1, 2
    prev_available_positions = set([(1, 1), (1, 2)])

    if n == 1 and (i, j) in prev_available_positions:
        return "YES"

    for _ in range(n-1):
        next_available_positions = set()
        for pos_i, pos_j in prev_available_positions:
            next_available_positions.add((pos_j, pos_i + fn))
            next_available_positions.add((pos_j, pos_i))

        fp, fn = fn, fn + fp
        prev_available_positions = next_available_positions
    
    if (i, j) in prev_available_positions:
        return "YES"
    return "NO"

 
t = int(input())
for _ in range(t):
    print(problem())


# 12
# 1 1 1
# 2 1 2
# 3 1 4
# 3 3 2
# 4 4 6
# 4 3 3
# 5 6 5
# 5 4 12
# 5 2 12
# 4 2 1
# 1 1 2
# 44 758465880 1277583853
