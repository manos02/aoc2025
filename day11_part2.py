from collections import defaultdict

file = open('input.txt', 'r')
lines = file.read().strip().split("\n")

devices = defaultdict(list)
SEEN = defaultdict(dict)

def solve(current, isfft, isdac):

    if current == 'svr' and isfft and isdac:
        return 1
    
    if (current, isfft, isdac) in SEEN:
        return SEEN[(current, isfft, isdac)]
    
    if current == 'fft':
        isfft = True
    if current == 'dac':
        isdac = True

    total = 0
    for val in devices[current]:
        total += solve(val, isfft, isdac)        

    SEEN[(current, isfft, isdac)] = total
    return total

for l in lines:
    input, output = l.split(":")
    for out in output.split():
        devices[out].append(input)


print(solve('out', False, False))

