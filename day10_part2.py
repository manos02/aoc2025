from ortools.sat.python import cp_model


file = open('input.txt', 'r')
lines = file.read().strip().split("\n")

def solve_linear_equations(buttons, combination):

    target = [int(c) for c in combination.split(",")]
    num_counters = len(target)
    num_buttons = len(buttons)
    max_target = max(target)

    model = cp_model.CpModel()
    presses = [model.NewIntVar(0, max_target, f"p{j}") for j in range(num_buttons)]

    for i in range(num_counters):
        affecting = [presses[j] for j, btn in enumerate(buttons) if i in btn]
        model.Add(sum(affecting) == target[i])

    model.Minimize(sum(presses))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
 
    return int(sum(solver.Value(v) for v in presses))




def process(buttons, n):
    buttons = [int(x) for x in buttons]
    return buttons

total = 0
for l in lines:
    t = l.split()
    combination = t.pop()
    t.pop(0)
    combination = (combination[1:len(combination)-1])
    buttons = list(map(lambda x: x[1:len(x)-1].split(","), t))
    buttons = [process(b, len(combination.split(","))) for b in buttons]
    total += solve_linear_equations(buttons, combination)

print(total)

