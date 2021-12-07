# https://adventofcode.com/2021/day/1
# https://adventofcode.com/2021/day/1/input

with open("input-data/advent-1.txt", "r") as f:
    data = f.readlines()

formatted_data = []

for val in data:
    new_val = val.rstrip("\n")
    formatted_data.append(int(new_val))

first_result = 0

for i in range(1, len(formatted_data)):
    if formatted_data[i] > formatted_data[i - 1]:
        first_result += 1

print(first_result)

fd = formatted_data
result = 0

for i in range(3, len(fd)):
    if fd[i] + fd[i - 1] + fd[i - 2] > fd[i - 1] + fd[i - 2] + fd[i - 3]:
        result += 1

print(result)