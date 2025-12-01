# solution 1
file = open('input2.txt', 'r')
lines = file.read().strip().split()
current, total = 50, 0

for l in lines:
    num = int(l[1::])
    
    for _ in range(num):
        current = (current + 1 if l[0] == "R" else current - 1) % 100
        
        if current == 0:
            total += 1

print(total)        



