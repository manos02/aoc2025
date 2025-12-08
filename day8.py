from collections import defaultdict
import math


file = open('input.txt', 'r')
boxes = file.read().strip().split()

rest = [tuple(map(int, b.split(','))) for b in boxes]

def s_line_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

lowest = []
for i, box in enumerate(rest):
    x, y, z = box
    for j in range(i + 1, len(rest)):
        if i == j:
            continue

        d = s_line_distance(box, rest[j])
        lowest.append((box, rest[j], d))

lowest = sorted(lowest, key=lambda x: x[2])

n = len(rest)
parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

for box1, box2, _ in lowest[:1000]:
    i = rest.index(box1)
    j = rest.index(box2)
    union(i, j)

components = sorted({find(i): size[find(i)] for i in range(n)}.values(), reverse=True)
print(math.prod(components[:3]))