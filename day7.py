from collections import defaultdict


file = open('input.txt', 'r')
grid = file.read().strip().split()

def p(values):
    print('\n'.join(' '.join(str(x) for x in row) for row in values))

for i, r in enumerate(grid):
    for j, c in enumerate(r):
        if c == 'S':
            start = (i,j)


SEEN = defaultdict(dict)

def find(current):
    
    count = 0
    row, col = current
    
    if (row, col) in SEEN:
        return count

    SEEN[(row, col)] = True
    
    # out of boundaries
    if row == len(grid) or col > len(grid[0]) or col < 0:
        return count

    # the end is not reached
    if grid[row][col] == "." or grid[row][col] == "S":
        return find((row+1, col))
    
    elif grid[row][col] == "^":
        count += 1
        res = find((row, col+1)) + find((row, col-1))
        return res + count

    
print(find((start)))

