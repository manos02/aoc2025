from collections import defaultdict
import itertools

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

    return current

def generate_graph(len_combination, buttons):
    graph = defaultdict(list)
    combinations = list(itertools.product(['#', '.'], repeat=len_combination))
    combinations = list(map(lambda x: ''.join(x), combinations))
    for comb in combinations:
        for button in buttons:
            res = press(comb, button)
            if res != comb:
                graph[comb].append(res)
    
    return graph
    


def bfs(graph, node, target): #function for BFS
    visited = defaultdict(dict) # List for visited nodes.
    queue = []     #Initialize a queue
    if node == target:
        return 0
    visited[node] = 0
    queue.append( node)
    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        count = visited[m]
        if m == target:
            return count

        for neighbour in graph[m]:
            if neighbour not in visited:

                visited[neighbour] = count + 1
                queue.append(neighbour)

total = 0
for l in lines:
    t = l.split()
    t.pop()
    combination = t.pop(0)
    buttons = t[::]
    combination = combination[1:len(combination)-1]
    buttons = list(map(lambda x: x[1:len(x)-1].split(","), buttons))
    graph = generate_graph(len(combination), buttons)
    total += bfs(graph, "." * len(combination), combination)

print(total)