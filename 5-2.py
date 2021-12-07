# https://adventofcode.com/2021/day/5
# https://adventofcode.com/2021/day/5/input

with open("input-data/advent-5.txt", "r") as f:
    data = f.readlines()

formatted_data = []

for val in data:
    new_val = val.rstrip("\n")
    start_coord = new_val.split(" -> ")[0]
    end_coord = new_val.split(" -> ")[1]
    start_x = start_coord.split(",")[0]
    start_y = start_coord.split(",")[1]
    end_x = end_coord.split(",")[0]
    end_y = end_coord.split(",")[1]
    line = [int(start_x), int(start_y), int(end_x), int(end_y)]
    if line[0] == line[2] or line[1] == line[3]:
        if line[0] > line[2]:
            temp = line[2]
            line[2] = line[0]
            line[0] = temp
            del temp
        if line[1] > line[3]:
            temp = line[3]
            line[3] = line[1]
            line[1] = temp
            del temp
    formatted_data.append(line)

column = [0 for i in range(1000)]
grid = [list(column) for i in range(1000)]

checked = []

for sect in formatted_data:
    if sect[0] == sect[2]:
        checked.append(sect)
        for x in range(sect[1], sect[3] + 1):
            grid[sect[0]][x] = grid[sect[0]][x] + 1
    elif sect[1] == sect[3]:
        checked.append(sect)
        for x in range(sect[0], sect[2] + 1):
            grid[x][sect[1]] = grid[x][sect[1]] + 1


for data in checked:
    if data in formatted_data:
        formatted_data.remove(data)


part_one = 0

for line in grid:
    for i in line:
        if i >= 2:
            part_one += 1

print(part_one)


for sect in formatted_data:
    range_one = list(range(sect[0], sect[2] + 1, 1))
    range_two = list(range(sect[1], sect[3] + 1, 1))
    if sect[0] > sect[2]:
        range_one = list(range(sect[0], sect[2] - 1, -1))
    if sect[1] > sect[3]:
        range_two = list(range(sect[1], sect[3] - 1, -1))
    for a, b in zip(range_one, range_two):
        grid[a][b] = grid[a][b] + 1


total = 0

for line in grid:
    for i in line:
        if i >= 2:
            total += 1

print(total)
