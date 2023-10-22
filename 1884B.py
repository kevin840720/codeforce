# -*- encoding: utf-8 -*-
"""
@File:
    1884A.py
@Time:
    2023/10/22 15:08:16
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1884/problem/B
    .input-template | .py-template.py
@Status:
    AC
"""

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = input().strip()
    idx = -1
    ans = [0 for _ in range(x.count("0"))] + [-1 for _ in range(x.count("1"))]
    count_1 = 0
    for digit in x[::-1]:
        if digit == "0":
            idx += 1
            if idx == 0:
                ans[idx] = count_1
            else: 
                ans[idx] = count_1 + ans[idx-1]
        elif digit == "1":
            count_1 += 1
    print(" ".join(map(str, ans)))
    

