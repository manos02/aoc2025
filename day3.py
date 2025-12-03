file = open('input.txt', 'r')
lines = file.read().strip().split()

total = 0
for l in lines:
    max = -1
    for a in range(len(l)-1):
        for b in range(a+1, len(l)):
            if int(l[a]+l[b]) > max:
                max = int(l[a]+l[b])        
    total += max
print(total)