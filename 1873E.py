# -*- encoding: utf-8 -*-
"""
@File:
    1873E.py
@Time:
    2023/09/21 22:59:13
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/contest/1873/problem/E
"""
from collections import Counter
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = map(int, input().split())
    counter = sorted(Counter(a).items())
    cumsum = [0] + [0 for _ in range(len(counter))]
    cumsum2 = [0] + [0 for _ in range(len(counter))]
    flag = 0
    for idx in range(1, len(counter)+1):
        cumsum[idx] = cumsum[idx-1] + counter[idx-1][1]
        if idx == 1:
            cumsum2[idx] = cumsum2[idx-1] + cumsum[idx] + (counter[idx-1][0] - 1)*cumsum[idx-1]
        else:
            cumsum2[idx] = cumsum2[idx-1] + cumsum[idx] + (counter[idx-1][0] - counter[idx-2][0] - 1)*cumsum[idx-1]
        if cumsum2[idx] > x:
            flag = 1
            break
    if flag == 1:
        avail_corals = [counter[i][0]*counter[i][1] for i in range(idx-1)]
        ans = (sum(avail_corals)+x)//sum([counter[i][1] for i in range(idx-1)])
    elif flag == 0:
        avail_corals = [counter[i][0]*counter[i][1] for i in range(len(counter))]
        ans = (sum(avail_corals)+x)//n
    print(ans)

    