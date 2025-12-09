
file = open('input.txt', 'r')
lines = file.read().strip().split()
lines = [list(map(int, l.split(','))) for l in lines]

def d(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def find_area(p1, p2):
    return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)

max_d = -1
max_points = None
for r in range(len(lines)):
    for c in range(r+1, len(lines)):
        cd = d(lines[r], lines[c])
        if cd > max_d:
            max_d = cd
            max_points = (lines[r], lines[c])
            
print(find_area(max_points[0], max_points[1]))