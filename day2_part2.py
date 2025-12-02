file = open('input.txt', 'r')
str_file = file.read().strip()

ranges = list(map(lambda x: x.strip(), str_file.split(",")))
total = 0


def indalid_ids(string, str_len):
    total = 0
    for i in range(1, str_len+1):
        split_string_list = [string[x:x+i] for x in range(0,len(string),i)]
        if len(split_string_list) > 1 and all(item == split_string_list[0] for item in split_string_list):
            total += int(string)
            break

    return total

for r in ranges:
    temp = r.split("-")
    lower, upper = int(temp[0]), int(temp[1])
    for num in range(lower, upper+1):
        num_str = str(num)
        number_len = len(num_str)        
        total += indalid_ids(num_str, len(num_str))

print(total)