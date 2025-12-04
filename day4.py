file = open('input.txt', 'r')
lines = file.read().strip().split()
count = 0

adj = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (lines[row][col] == '.'):
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
            count += 1

print(count)