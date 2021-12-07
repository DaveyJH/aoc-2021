# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2/input

with open("input-data/advent-2.txt", "r") as f:
    origin_data = f.readlines()

formatted_data = []

for val in origin_data:
    new_val = val.rstrip("\n")
    formatted_data.append(new_val)

# Part 1
#######################################
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

# part 2
#######################################
x_pos = 0
y_pos = 0
aim = 0

for data in formatted_data:
    if "forward" in data:
        x_pos = x_pos + int(data[data.index(" "):])
        y_pos = y_pos + aim * int(data[data.index(" "):])
    elif "down" in data:
        aim = aim + int(data[data.index(" "):])
    elif "up" in data:
        aim = aim - int(data[data.index(" "):])

print(x_pos * y_pos)
