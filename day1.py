file = open('input.txt', 'r')
lines = file.read().strip().split()
current, total = 50, 0

for l in lines:
    num = int(l[1::])
    current = (current + num if l[0] == "R" else current - num) % 100
    if current == 0:
        total += 1

print(total)