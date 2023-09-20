# -*- encoding: utf-8 -*-
"""
@File:
    1867B.py
@Time:
    2023/09/15 11:36:35
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1867/B
"""


for I in range(int(input())):
    n = int(input())
    binary = input()
    odd = 0
    even = 0
    for i in range(n//2):
        if binary[i] == binary[n-1-i]:
            even += 1
        else:
            odd += 1

    if n%2 == 0:
        possible = [odd+i for i in range(0, 2*(even+1), 2)]
    elif n%2 == 1:
        possible = [odd+i for i in range(0, 2*(even+1))]
    result = ["1" if idx in possible else "0" for idx in range(n+1)]
    print("".join(result))