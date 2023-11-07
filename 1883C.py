# -*- encoding: utf-8 -*-
"""
@File:
    1883C.py
@Time:
    2023/10/22 19:56:52
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1883/problem/C
    .input-template | .py-template.py
@Status:
    Pretests passed (5)
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    if k in {2,3,5}:
        aaa = min(ai, key=lambda x: k - x%k if x%k != 0 else 0)
        ans = k-aaa%k if aaa%k != 0 else 0
    elif k == 4:
        if n == 1:
            ans = k-ai[0]%k if ai[0]%k != 0 else 0
        elif n > 1:
            bi = list(map(lambda x: x%2, ai))
            ci = list(map(lambda x: x%4, ai))
            max_ai = max(ai)
            if ci.count(0) >= 1:
                ans = 0
            elif bi.count(0) >= 2:
                ans = 0
            elif ci.count(3) >= 1:
                ans = 1
            elif bi.count(0) == 1:
                ans = 1
            elif bi.count(0) == 0:
                ans = 2
    print(ans)


