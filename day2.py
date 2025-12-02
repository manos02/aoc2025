file = open('input.txt', 'r')
str_file = file.read().strip()

ranges = list(map(lambda x: x.strip(), str_file.split(",")))
total = 0

for r in ranges:
    temp = r.split("-")
    lower, upper = int(temp[0]), int(temp[1])
    for num in range(lower, upper+1):
        num_str = str(num)
        number_len = len(num_str)
        if number_len % 2 == 0 and num_str[:(number_len // 2)] == num_str[(number_len // 2):]:
            total += num

print(total)