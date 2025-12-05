ranges = []
values = []

in_second_block = False

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:            
            in_second_block = True
            continue
        if in_second_block:
            values.append(int(line))
        else:
            con = lambda a : (int(a[0]),int(a[1]))
            ranges.append(con(line.split("-")))

total = 0
for v in values:
    for p in ranges:
        if v >= p[0] and v <= p[1]:
            total += 1
            break
print(total)