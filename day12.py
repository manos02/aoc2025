file = open('input.txt', 'r')
lines = file.read().strip().split("\n\n")

regions = lines[-1].split("\n")

lines.pop(-1)

shapes = []
res = 0

for l in lines:
    t = l.split(":")[-1]
    t = t.strip().split("\n")
    t = [[x for x in row if x == '#'] for row in t]
    total = sum(len(row) for row in t)
    shapes.append(total)

for r in regions:
    r = r.split()
    dimensions = r[0]
    presents = r[1::]
    
    dimensions = dimensions[:len(dimensions)-1]
    dimensions = dimensions.split("x")
    x = int(dimensions[0])
    y = int(dimensions[1])

    grid_size = x*y
    total_size = sum([shapes[i] * int(x) for i, x in enumerate(presents)])
    if total_size < grid_size:
        res += 1
        
print(res)