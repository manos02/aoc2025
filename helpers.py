
# read input
file = open('input.txt', 'r')
lines = file.read().strip().split()

# print 2d grid
def p(values):
    print('\n'.join(' '.join(str(x) for x in row) for row in values))