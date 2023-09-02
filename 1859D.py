# -*- encoding: utf-8 -*-
"""
@File:
    1859D.py
@Time:
    2023/09/02 20:29:34
@Author:
    Kevin Wang
@Desc:
    https://codeforces.com/problemset/problem/1859/D
"""

from time import time
def check_portal_i_to_j(portal_i, portal_j):
    if (portal_j[0] <= portal_i[1] <= portal_j[3]) or (portal_j[0] <= portal_i[2] <= portal_j[3]):
        return True
    return False

def get_connect_component(init, visited:list, matrix):
    n = len(matrix)
    neighbors = set([i for i in range(n) if ((matrix[i][init] == 1) or (matrix[init][i] == 1))])
    visited.append(init)
    connected_component = neighbors
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        connected_component.union(get_connect_component(neighbor, visited, matrix))
    return connected_component

def get_dsu(matrix):
    dsu = []
    undetermined = set(range(len(matrix)))
    while undetermined:
        connect_component = get_connect_component(undetermined.pop(), [], matrix)
        dsu.append(connect_component)
        undetermined.difference_update(connect_component)
    return dsu

def is_in_portal(init, portal:list):
    if portal[0] <= init <= portal[3]:
        return True
    return False

def problem():
    # Input
    num_of_portal = int(input())
    portals = []
    for _ in range(num_of_portal):
        l, r, a, b = input().strip("\n").split(" ")
        portals.append([int(_) for _ in [l, a, b, r]])
    num_of_entry = int(input())
    entries = [int(_) for _ in input().strip("\n").split(" ")]

    # Create directed graph
    b = time()
    a = time()
    print(b-a)
    matrix = [[0 for _ in range(num_of_portal)] for _ in range(num_of_portal)]
    for i in range(num_of_portal):
        for j in range(num_of_portal):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = int(check_portal_i_to_j(portals[i], portals[j]))

    # DSU
    # dsu = get_dsu(matrix)

    # Consider if we start at one portal, how far can we get
    farest_portal_position = [None for i in range(len(matrix))]
    def go_far_as_you_can(init, visited:list):
        current_far = portals[init][2]
        neighbors = set([i for i in range(num_of_portal) if (matrix[init][i] == 1)])
        visited.append(init)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if farest_portal_position[neighbor] != None:
                current_far = max(current_far, farest_portal_position[neighbor])
            else:
                current_far = max(current_far, go_far_as_you_can(neighbor, visited))
        return current_far

    for i in range(len(matrix)):
        farest_portal_position[i] = go_far_as_you_can(i, [])

    # Consider if we start at arbitrary point, how far can we get
    farest_position = []
    for entry in entries:
        farest = max([entry] + [farest_portal_position[idx] for idx in range(num_of_portal) if is_in_portal(entry, portals[idx])])
        farest_position.append(farest)

    print(" ".join([str(_) for _ in farest_position]))

t = int(input())
for _ in range(t):
    problem()
