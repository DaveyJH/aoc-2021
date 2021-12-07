# https://adventofcode.com/2021/day/1
# https://adventofcode.com/2021/day/1/input

with open("input-data/advent-1.txt", "r") as f:
    data = f.readlines()

formatted_data = []

for val in data:
    new_val = val.rstrip("\n")
    formatted_data.append(int(new_val))

result = 0

for i in range(1, len(formatted_data)):
    if formatted_data[i] > formatted_data[i - 1]:
        result += 1

print(result)
