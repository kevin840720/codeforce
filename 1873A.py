# -*- encoding: utf-8 -*-
"""
@File:
    1873A.py
@Time:
    2023/09/21 22:35:57
@Author:
    Kevin Wang
@Desc:
    None
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()
    if (s[0] != "a") and (s[1] != "b") and (s[2] != "c"):
        print("NO")
    else:
        print("YES")