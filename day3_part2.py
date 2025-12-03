file = open('input.txt', 'r')
lines = file.read().strip().split()


def find_biggest(l):
    digits_remaining = 12
    found_index = 0
    current_index = -1
    res = ''
    for _ in range(12):
        temp_max = -1
        for j in range(current_index+1, len(l)-digits_remaining+1):
            if (int(l[j]) > temp_max):
                temp_max = int(l[j])
                found_index = j
        current_index = found_index
        res += l[current_index]
        digits_remaining -= 1
    return int(res)


total = 0
for l in lines:

    total += find_biggest(l)

print(total)

