import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

file = open('input.txt', 'r')
lines = file.read().strip().split('\n')

g = [l.split() for l in lines]

totals = list(zip(list(map(int, g[0])), g[-1]))


for i in range(1, len(g)-1):
    for j in range(len(g[0])):
        a, s = totals[j]
        new_t = (ops[s](a, int(g[i][j])), s)
        totals[j] = new_t

print(sum(list(map(lambda x: x[0], totals))))

