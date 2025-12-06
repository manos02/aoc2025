ranges = []

with open("input2.txt") as f:
    for line in f:
        line = line.strip()
        if not line:            
            break
        else:
            con = lambda a : (int(a[0]),int(a[1]))
            ranges.append(con(line.split("-")))


def red(ra, change=True):
    while True:
        if not change:
            break
        change = False    
        for j in range(len(ra)):
            if ra[j] == None:
                continue
            l1, h1 = ra[j]
            for i in range(len(ra)):
                if j == i or ra[i] == None:
                    continue
                l2, h2 = ra[i]
                if l1 >= l2 and l1 <= h2 and h1 > h2:
                    ra[i] = (l2, h1)
                    ra[j] = None
                    change = True

                if l1 < l2 and h1 >= l2 and h1 <= h2:
                    ra[i] = (l1, h2)
                    ra[j] = None
                    change = True
                
                if l1 < l2 and h1 > h2:
                    ra[i] = (l1, h1)
                    ra[j] = None
                    change = True
    return ra
    
filtered = list(set([x for x in red(ranges) if x is not None]))


print(sum(t[1]+1 - t[0] for t in filtered))
        


        




