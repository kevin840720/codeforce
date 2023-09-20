# -*- encoding: utf-8 -*-
"""
@File:
    1850C.py
@Time:
    2023/09/19 21:41:18
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1850/problem/C
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    string = ""
    for i in range(8):
        string += input().strip().replace(".", "")
    print(string)