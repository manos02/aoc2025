from collections import defaultdict

file = open('input.txt', 'r')
lines = file.read().strip().split("\n")

devices = defaultdict(list)
def solve(current):

    if current == 'out':
        return 1
    
    total = 0
    for val in devices[current]:
        total += solve(val)        

    return total

for l in lines:
    input, output = l.split(":")
    devices[input] = output.split()

print(solve('you'))

