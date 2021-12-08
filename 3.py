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


def filter_by_bits(index, current_data, oxy=True):

    bit_counter = 0

    for data in current_data:
        if data[index] == "0":
            bit_counter = bit_counter - 1
        elif data[index] == "1":
            bit_counter = bit_counter + 1
    if bit_counter >= 0:
        if oxy:
            bit = "1"
        else:
            bit = "0"
    else:
        if oxy:
            bit = "0"
        else:
            bit = "1"

    inner_results = []

    for data in current_data:
        if data[index] == bit:
            inner_results.append(data)

    return inner_results


results = filter_by_bits(0, formatted_data)
x = 1
while len(results) > 1:
    results = filter_by_bits(x, results)
    x += 1
oxygen = int(results[0], 2)

results = filter_by_bits(0, formatted_data, False)
x = 1
while len(results) > 1:
    results = filter_by_bits(x, results, False)
    x += 1
co2 = int(results[0], 2)

print(oxygen * co2)
