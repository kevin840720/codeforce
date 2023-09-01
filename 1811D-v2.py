# -*- encoding: utf-8 -*-
"""
@File    :  1811D-v2.py
@Time    :  2023/04/10 10:53:57
@Author  :  Kevin Wang
@Desc    :  用 Pypy 才會過
"""
Fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
         75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
         39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]

# def fibonacci(n):
    # seq = [1, 1]
    # for _ in range(n-1):
    #     seq.append(seq[-1] + seq[-2])
    # return seq[1:]

def problem():
    n, i, j = [int(_) for _ in input().split()]
    fn = Fib[1:n+1]

    for width, square_len in zip(fn[1:][::-1], fn[:-1][::-1]):
        if 0 <= j <= width - square_len:
            i, j = j, i
        elif  square_len < j <= width:
            i, j = j - square_len, i
        else:
            return "NO"

    return "YES"

t = int(input())
for _ in range(t):
    print(problem())

# 12
# 1 1 1
# 2 1 2
# 3 1 4
# 3 3 2
# 4 4 6
# 4 3 3
# 5 6 5
# 5 4 12
# 5 2 12
# 4 2 1
# 1 1 2
# 44 758465880 1277583853

# YES
# NO
# YES
# YES
# YES
# NO
# YES
# NO
# NO
# YES
# YES
# NO



