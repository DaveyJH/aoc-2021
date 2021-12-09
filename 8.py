# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/8
# https://adventofcode.com/2021/day/8/input

with open("input-data/advent-8.txt", "r") as f:
    data = f.readlines()

formatted_data = []

for line in data:
    line.rstrip("\n")
    patterns, digits = line.split("|")
    patterns = patterns.strip()
    digits = digits.strip()
    formatted_data.append([patterns, digits])

total = 0

for line in formatted_data:
    key = ["" for i in range(10)]
    line[0] = list(line[0].split(" "))
    line[1] = list(line[1].split(" "))
    for i, lst in enumerate(line):
        for j, string in enumerate(line[i]):
            line[i][j] = "".join(sorted(string))
    # length specific digits
    for i in line[0]:
        if len(i) == 2:
            key[1] = i
        elif len(i) == 3:
            key[7] = i
        elif len(i) == 4:
            key[4] = i
        elif len(i) == 7:
            key[8] = i
    # uses 1, 7, 4, 8 and unique line
    for i in line[0]:
        if len(i) == 6:
            if all(char in i for char in key[4]):
                key[9] = i
            elif all(char in i for char in key[7]):
                key[0] = i
            else:
                key[6] = i
    # checks letter of lower-left line unique to 2
    # uses 9
    lower_left = tuple(set(key[8]) ^ set(key[9]))[0]
    # uses lower_left and 7
    for i in line[0]:
        if len(i) == 5:
            if all(char in i for char in key[7]):
                key[3] = i
            elif lower_left in i:
                key[2] = i
            else:
                key[5] = i
    number = ""
    # check sorted string index in key for value
    for d in line[1]:
        number = number + str(key.index(d))
    number = int(number)
    total = total + number

print(total)
