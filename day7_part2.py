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
    
    row, col = current

    if (row, col) in SEEN:
        return SEEN[(row, col)]

    # end is reached
    if row == len(grid) - 1:
        return 1
    
    # out of boundaries
    if row == len(grid) or col > len(grid[0]) or col < 0:
        return 

    # the end is not reached
    if grid[row][col] == "." or grid[row][col] == "S":
        return find((row+1, col))
    
    elif grid[row][col] == "^":
        res = find((row, col+1)) + find((row, col-1))
        SEEN[(row, col)] = res
        return res

    
print(find((start)))

