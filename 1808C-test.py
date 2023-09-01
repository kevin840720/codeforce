# -*- encoding: utf-8 -*-
"""
@File    :  1808C-test.py
@Time    :  2023/04/17 12:00:08
@Author  :  Kevin Wang
@Desc    :  None
"""

from typing import List
from pathlib import Path
import subprocess

from random import randint

here = Path(__file__)
FILEPATH = Path(here.parent, "1808C.py").__str__()

def lucky(num):
    num_set = set([int(_) for _ in str(num)])
    return max(num_set) - min(num_set)

def calc(a, b):
    best_luckiness = 999
    best_number = None
    for num in range(a, b+1):
        luckiness = lucky(num)
        if luckiness < best_luckiness:
            best_luckiness = luckiness
            best_number = num
    return best_number

# def simulate(t=1000):
#     string = f"{t}".encode() + b"\n"
#     inputs = []
#     answer = []
#     for i in range(t):
#         b = randint(2, 10**5)
#         a = randint(1, b)
#         string += f"{a} {b}".encode() + b"\n"
#         inputs.append((a, b))
#         answer.append(calc(a, b))
#     return string, inputs, answer

def simulate():
    string = b""
    inputs = []
    answer = []
    for a in range(800, 1000):
        for b in range(a, 1000):
            string += f"{a} {b}".encode() + b"\n"
            inputs.append((a, b))
            answer.append(calc(a, b))
    string = f"{len(inputs)}".encode() + b"\n" + string
    return string, inputs, answer

input_binary_str, simulated_input, simulated_answer = simulate()
result = subprocess.run(["python", FILEPATH], input=input_binary_str, capture_output=True)



def grade(raw_result:str, inputs, answers:List[int]):
    results = [int(_) for _ in raw_result.split()]
    for result, input, answer in zip(results, inputs, answers):
        if lucky(result) != lucky(answer):
            print("input: ", input, " | ", "result: ", result, " | ", "answer: ", answer)

grade(result.stdout.decode(), simulated_input, simulated_answer)
print(result.stderr.decode())