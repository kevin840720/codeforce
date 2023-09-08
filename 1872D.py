# -*- encoding: utf-8 -*-
"""
@File:
    1872D.py
@Time:
    2023/09/08 20:06:38
@Author:
    Kevin Wang
@Desc:
    None
"""

from math import lcm
def problem():
    n, x, y = [int(_) for _ in input().split()]
    add_count = round((n - n%x)/x)
    minus_count = round((n - n%y)/y)
    l = lcm(x, y)
    common_count = round((n - n%l)/l)

    eff_add_count = add_count - common_count
    eff_minus_count = minus_count - common_count

    if eff_add_count % 2 == 1:
        add = (n + round((- eff_add_count + 1)/2))*eff_add_count
    else:
        add = (2*n - eff_add_count + 1)*round(eff_add_count/2)

    if eff_minus_count % 2 == 1:
        minus = round((eff_minus_count + 1)/2)*eff_minus_count
    else:
        minus = (eff_minus_count + 1)*round(eff_minus_count/2)

    print(add-minus)


t = int(input())
for _ in range(t):
    problem()
