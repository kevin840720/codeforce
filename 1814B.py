# -*- encoding: utf-8 -*-
"""
@File    :  1814B.py
@Time    :  2023/04/13 11:29:51
@Author  :  Kevin Wang
@Desc    :  None
"""

def how_many_action(a, b, m):
    qa, ra = divmod(a, m)
    qb, rb = divmod(b, m)
    return (m - 1) + qa + qb + (1 if ra > 0 else 0) + (1 if rb > 0 else 0)

def problem():
    a, b = [int(_) for _ in input().split()]
    """
    若假設連續並給定腿長 m ，可以得出總步數為 f(m) = a/m + b/m + m - 1
    最小值則落在 m = sqrt(a+b)

    回到整數情況的 m，若 a÷m 有餘數，則餘數算額外一步（b 同理），所以最糟的情況是 a, b 都有餘數 -> 多兩步
    求解 f(m) = f(m*) + 2 -> 得到一個範圍，即 (rng_min, rng_max)
    從中遍瀝最少步數解
    """
    cont = pow(a+b, 0.5)
    rng_min = cont + 1 - pow(2*cont + 1, 0.5)
    rng_max = cont + 1 + pow(2*cont + 1, 0.5)
    candidates = [how_many_action(a, b, m) for m in range(int(rng_min), int(rng_max)+1) if m > 0]

    return min(candidates)

t = int(input())
for _ in range(t):
    print(problem())

# 32848823 374682702
