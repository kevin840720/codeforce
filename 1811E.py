# -*- encoding: utf-8 -*-
"""
@File    :  1811E.py
@Time    :  2023/04/10 11:40:30
@Author  :  Kevin Wang
@Desc    :  None
"""
digits = "012356789"

def problem():
    k = int(input())
    num = []
    q = k
    while q > 0:
        q, r = divmod(q, 9)
        num.append(r)
    return "".join([digits[r] for r in num[::-1]])

t = int(input())
for _ in range(t):
    print(problem())

# 7
# 3
# 5
# 22
# 10
# 100
# 12345
# 827264634912

# 3
# 6
# 25
# 11
# 121
# 18937
# 2932285320890
