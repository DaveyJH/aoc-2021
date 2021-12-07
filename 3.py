# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3/input

with open("input-data/advent-3.txt", "r") as f:
    origin_data = f.readlines()

formatted_data = []

for val in origin_data:
    new_val = val.rstrip("\n")
    formatted_data.append(new_val)

counts = {i: 0 for i in range(len(formatted_data[0]))}

for data in formatted_data:
    for i in range(len(data)):
        if data[i] == "1":
            counts[i] = counts[i] + 1
        else:
            counts[i] = counts[i] - 1

gamma = ""
epsilon = ""
for value in counts.values():
    if value >= 0:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

gamma_base10 = int(gamma, 2)
epsilon_base10 = int(epsilon, 2)

print(gamma_base10 * epsilon_base10)
