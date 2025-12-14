from collections import defaultdict
import itertools

file = open('input.txt', 'r')
lines = file.read().strip().split("\n")


def solve_linear_equations(buttons, combination):
    
    pass


def process(buttons, n):
    buttons = [int(x) for x in buttons]
    # buttons.extend([0] * (n - len(buttons)))
    return buttons

total = 0
for l in lines:
    t = l.split()
    combination = t.pop()
    t.pop(0)
    combination = combination[1:len(combination)-1]
    buttons = list(map(lambda x: x[1:len(x)-1].split(","), t))
    buttons = [process(b, len(combination.split(","))) for b in buttons]
    solve_linear_equations(buttons, combination)
    break
    # total += bfs(graph, "." * len(combination), combination)

# print(total)