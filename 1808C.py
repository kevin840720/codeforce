# -*- encoding: utf-8 -*-
"""
@File    :  1808C.py
@Time    :  2023/04/14 13:35:29
@Author  :  Kevin Wang
@Desc    :  None
"""
# -*- encoding: utf-8 -*-
"""
@File    :  1808C.py
@Time    :  2023/04/14 13:35:29
@Author  :  Kevin Wang
@Desc    :  None
"""

def max_prefix(str1, str2):
    prefix = ""
    for x, y in zip(str1, str2):
        if x == y:
            prefix += x
        else:
            break
    return prefix, str1[len(prefix):], str2[len(prefix):]

def luckiness(string:str):
    digits = set(int(_) for _ in string)
    return max(digits) - min(digits)

def view_above(string:str, prefix_set:set):
    assert len(string) >= 2

    lead = string[0]
    m = min(prefix_set.union([int(string[0])]))
    if m < int(string[1]):
        candidate = lead + str(m)*(len(string)-1)
    elif m == int(string[1]):
        if int(lead + str(m)*(len(string)-1)) <= int(string):
            candidate = lead + str(m)*(len(string)-1)
        else:
            candidate = lead + str(m-1)*(len(string)-1)
    else: # m > int(string[1])
        if int(lead + string[1]*(len(string)-1)) <= int(string):
            candidate = lead + string[1]*(len(string)-1)
        else:
            candidate = lead + str(int(string[1])-1)*(len(string)-1)
    return candidate

def view_mid(string1:str, string2:str, prefix_set:set):
    assert len(string1) >= 2
    assert int(string1) < int(string2)
    assert int(string1[0]) + 2 <= int(string2[0])

    M, m = max(prefix_set), min(prefix_set)
    candidate = str(int(string1[0])+1)*len(string1)
    candidate_luck = max(M, int(string1[0])+1) - min(m, int(string1[0])+1)
    for digit in range(int(string1[0])+2, int(string2[0])):
        luck = max(M, digit) - min(m, digit)
        if luck < candidate_luck:
            candidate = str(digit)*len(string1)
            candidate_luck = luck
    return candidate

def view_below(string:str, prefix_set:set):
    assert len(string) >= 2

    lead = string[0]
    M = max(prefix_set.union([int(string[0])]))
    if M > int(string[1]):
        candidate = lead + str(M)*(len(string)-1)
    elif M == int(string[1]):
        if int(lead + str(M)*(len(string)-1)) >= int(string):
            candidate = lead + str(M)*(len(string)-1)
        else:
            candidate = lead + str(M+1)*(len(string)-1)
    else: # M < int(string[1])
        if int(lead + string[1]*(len(string)-1)) >= int(string):
            candidate = lead + string[1]*(len(string)-1)
        else:
            candidate = lead + str(int(string[1])+1)*(len(string)-1)
    return candidate

def problem():
    l, r = input().split()

    # early exit
    if l == r:
        return l
    if len(l) != len(r):
        return "9"*(max(len(l), len(r))-1)
    if int(l[0]) + 2 <= int(r[0]):
        return str(int(l[0])+1)*len(l)

    prefix, l, r = max_prefix(l, r)
    if len(l) >= 2:
        prefix_set = set(int(_) for _ in prefix)
        candidate_above = view_above(r, prefix_set)
        candidate_below = view_below(l, prefix_set)
        if int(r[0]) - int(l[0]) >= 2:
            candidate_mid = view_mid(l, r, prefix_set)
            best = min([prefix + candidate_above, prefix + candidate_mid, prefix + candidate_below], key=luckiness)
        else:
            best = min([prefix + candidate_above, prefix + candidate_below], key=luckiness)
    elif len(l) == 1:
        best = int(prefix + l)
        best_luckiness = luckiness(prefix + l)
        for last in range(int(l), int(r)+1):
            candidate = prefix + str(last)
            luck = luckiness(candidate)
            if luck < best_luckiness:
                best_luckiness = luck
                best = candidate
    return best

t = int(input())
for _ in range(t):
    print(problem())