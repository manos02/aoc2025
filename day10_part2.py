from collections import defaultdict
import itertools
import numpy as np
from ortools.sat.python import cp_model

file = open('input.txt', 'r')
lines = file.read().strip().split("\n")


def solve_linear_equations(buttons, combination):

    equations = defaultdict(list)
    combination = [int(c) for c in combination.split(",")]
    
    # print(buttons, combination)
    for i, c in enumerate(combination):
        for b in buttons:
            if i not in b:
                equations[i].append(0)
                continue
            equations[i].append(1)
            # for num in b:


    val = [combination[i] for i in equations.keys()]
    a = np.array(list(equations.values()))
    b = np.array(val)

    # solve 2 linear equations



def process(buttons, n):
    buttons = [int(x) for x in buttons]
    # buttons.extend([0] * (n - len(buttons)))
    return buttons

total = 0
for l in lines:
    t = l.split()
    combination = t.pop()
    t.pop(0)
    combination = (combination[1:len(combination)-1])
    buttons = list(map(lambda x: x[1:len(x)-1].split(","), t))
    buttons = [process(b, len(combination.split(","))) for b in buttons]
    solve_linear_equations(buttons, combination)
    break
    # total += bfs(graph, "." * len(combination), combination)

# print(total)


'''
a + b + d = 7
b + 

'''