file = open('input.txt', 'r')
lines = file.read().strip().split()
count = 0


adj = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def p(values):
    print('\n'.join(' '.join(str(x) for x in row) for row in values))

def rep(indices):
    for (x, y) in indices:
        str_to_replace = lines[x]
        new_str = str_to_replace[:y] + "." + str_to_replace[y+1:]
        lines[x] = new_str     

def find(end_row, end_col):
    count = 0
    while True:
        indices_to_replace = []
        change = False
        for row in range(end_row):   
            for col in range(end_col):    
                if (lines[row][col] == '.' or lines[row][col] == 'x'):
                    continue
                temp = 0
                for pos in adj:
                    x, y = pos
                    temp_row = row + x
                    temp_col = col + y
                    if temp_col < 0 or temp_col >= len(lines[0]) or temp_row < 0 or temp_row >= len(lines):
                        continue
                    if lines[temp_row][temp_col] == '@':
                        temp += 1
                if temp < 4:
                    change = True
                    count += 1
                    indices_to_replace.append((row, col))
        rep(indices_to_replace)
        if not change:
            break
    return count


count = find(len(lines), len(lines))

print(count)