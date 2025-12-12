file = open('input.txt', 'r')
lines = file.read().strip().split("\n")


def press(current, combination):
    for c in combination:
        if current[int(c)] == "#":
            index = int(c)
            current = current[:index] + "." + current[index+1:]
        else:
            index = int(c)
            current = current[:index] + "#" + current[index+1:]


max = 1000000000000

def find_lowest(combination, current, buttons, steps):



    if current == combination:
        return steps
    
    # if steps > max:
    #     return 
    totals = []
    for i in range(len(buttons)):
        totals[i] = find_lowest(combination, press(current, buttons[i]), lights, steps+1)
        return min(totals[i])



for l in lines:
    t = l.split()
    t.pop()
    lights = t.pop(0)
    buttons = t[1:len(t)-1]
    lights = lights[1:len(lights)-1]
    buttons = list(map(lambda x: x[1:len(x)-1].split(","), buttons))
    print(buttons, lights)
    find_lowest(lights, "." * len(lights), buttons, 0)

    