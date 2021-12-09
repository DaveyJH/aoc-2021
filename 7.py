# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7/input

with open("input-data/advent-7.txt", "r") as f:
    data = f.readlines()

formatted_data = []

separate_strings = data[0].split(",")
for string in separate_strings:
    formatted_data.append(int(string))


def triangular_number(n):
    """Returns the nth triangular number"""

    return n*(n + 1) // 2


lowest = min(formatted_data)
highest = max(formatted_data)

results = {i: 0 for i in range(lowest, highest + 1)}

for i in range(lowest, highest + 1):
    inter_results = []
    for j in formatted_data:
        # result = abs(i - j)  # part 1
        result = triangular_number(abs(i - j))
        inter_results.append(result)
    results.update({i: sum(inter_results)})

for k, v in results.items():
    if v == min(results.values()):
        x_pos = k
        fuel = v

print(x_pos)
print(fuel)
