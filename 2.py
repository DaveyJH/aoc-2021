# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2/input

with open("input-data/advent-2.txt", "r") as f:
    origin_data = f.readlines()

formatted_data = []

for val in origin_data:
    new_val = val.rstrip("\n")
    formatted_data.append(new_val)

forward = 0
y_position = 0

for data in formatted_data:
    if "forward" in data:
        forward = forward + int(data[data.index(" "):])
    elif "down" in data:
        y_position = y_position + int(data[data.index(" "):])
    elif "up" in data:
        y_position = y_position - int(data[data.index(" "):])


print(forward * y_position)