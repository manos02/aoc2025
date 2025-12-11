from shapely.geometry import Polygon, box

file = open('input.txt', 'r')
lines = file.read().strip().split()
lines = [list(map(int, l.split(','))) for l in lines]

def find_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

MARKED = set()
s = sorted(lines, key = lambda x: (x[1], x[0]))

for p in range(0, len(s)-1, 2):
    col = s[p][0]
    row = s[p][1]
    next_p = s[p+1]
    for j in range(col, next_p[0]+1):
        MARKED.add((j, row))

s = sorted(lines, key = lambda x: (x[0], x[1]))


for p in range(0, len(s)-1, 2):
    col = s[p][0]
    row = s[p][1]
    next_p = s[p+1]
    for j in range(row, next_p[1]+1):
        MARKED.add((col, j))

def rectangle_from_diagonal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return [
        (x1, y2),
        (x2, y1)
    ]

max_d = -1
max_points = None
boundary = Polygon(lines)  
allowed_region = boundary.buffer(0.5, cap_style=2, join_style=2)

for r in range(len(lines)):
    for c in range(r+1, len(lines)):
        cd = find_area(lines[r], lines[c])

        points = rectangle_from_diagonal(lines[r], lines[c])

        min_x = min(lines[r][0], lines[c][0]) - 0.5
        max_x = max(lines[r][0], lines[c][0]) + 0.5
        min_y = min(lines[r][1], lines[c][1]) - 0.5
        max_y = max(lines[r][1], lines[c][1]) + 0.5
        rect = box(min_x, min_y, max_x, max_y)
        if cd > max_d and allowed_region.covers(rect):
            max_d = cd
            max_points = (lines[r], lines[c])
            
print(find_area(max_points[0], max_points[1]))