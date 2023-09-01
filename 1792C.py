# -*- encoding: utf-8 -*-
"""
@File    :  1792C.py
@Time    :  2023/02/13 21:42:58
@Author  :  Kevin Wang
@Desc    :  None
"""

def indexing(seq, ele):
    try:
        return seq.index(ele)
    except:
        return -1

def problem():
    count = int(input())
    sequence = [int(_) for _ in input().split()]

    if len(sequence)%2 == 1:
        center = len(sequence)//2+1
        pos = sequence.index(center)
        left_sequence = sequence[:pos]
        right_sequence = sequence[pos+1:]
        left = center - 1
        right = center + 1
        count = 0
    else:
        left = len(sequence)//2
        right = left + 1
        pos_left = indexing(sequence, left)
        pos_right = indexing(sequence, right)
        if pos_right <= pos_left:
            return len(sequence)//2
        left_sequence = sequence[:pos_left]
        right_sequence = sequence[pos_right+1:]
        count = 1
        left = left - 1
        right = right + 1


    if len(left_sequence) > 0 and len(right_sequence) > 0:
        left_sequence = left_sequence[::-1]
        max_left_viewed = -1
        min_right_viewed = len(sequence)+1
    while len(left_sequence) > 0 and len(right_sequence) > 0:
        if max_left_viewed == left: # early exit
            break
        if right == min_right_viewed: # early exit
            break

        pos_left = indexing(left_sequence, left)
        if pos_left < 0:
            break
        pos_right = indexing(right_sequence, right)
        if pos_right < 0:
            break

        # Next round preparation
        max_left_viewed = max(left_sequence[:pos_left] + [max_left_viewed])
        min_right_viewed = min(right_sequence[:pos_left] + [min_right_viewed])

        left_sequence = left_sequence[pos_left+1:]
        right_sequence = right_sequence[pos_right+1:]
        left = left - 1
        right = right + 1
        count += 1
    return len(sequence)//2 - count

t = int(input())
for _ in range(t):
    print(problem())