# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/11
# https://adventofcode.com/2021/day/11/input

from pprint import pprint

with open("input-data/advent-11.txt", "r") as f:
    data = f.readlines()

formatted_data = [line.rstrip("\n") for line in data]

flashes = 0


def create_grid(origin):
    """Create array of row arrays to represent grid"""

    new_grid = []
    for row in origin:
        int_row = []
        for octo in row:
            int_row.append(int(octo))
        new_grid.append(int_row)
    return new_grid


def add_one(current_grid):
    """Add one to all octos"""

    new_grid = []
    for row in current_grid:
        new_line = []
        for octo in row:
            octo += 1
            new_line.append(octo)
        new_grid.append(new_line)
    return new_grid


def check_surrounds(current_grid):
    """Check for octos to be manipulated and keep flash count"""

    flash_count = 0
    affected_octos = []
    flashing_octos = []

    for i, row in enumerate(current_grid):
        for j, octo in enumerate(row):
            if octo > 9:
                flashing_octos.append((i, j))
                flash_count += 1
                surround = []
                if i > 0:
                    surround.append((i - 1, j))
                    if j > 0:
                        surround.append((i - 1, j - 1))
                    if j < len(row) - 1:
                        surround.append((i - 1, j + 1))

                if j > 0:
                    surround.append((i, j - 1))
                if j < len(row) - 1:
                    surround.append((i, j + 1))

                if i < len(current_grid) - 1:
                    surround.append((i + 1, j))
                    if j > 0:
                        surround.append((i + 1, j - 1))
                    if j < len(row) - 1:
                        surround.append((i + 1, j + 1))
                affected_octos.append(surround)

    return affected_octos, flash_count, flashing_octos


def check_flashes(current_grid):
    """Check for grid changes according to flashes"""

    new_grid = list(i[:] for i in current_grid)

    global flashes
    surrounds_and_flashes = check_surrounds(current_grid)
    # add to flash count
    flashes += surrounds_and_flashes[1]
    # create lis of coords
    adjustment_octos = []
    for i in surrounds_and_flashes[0]:
        adjustment_octos.extend(i)

    reset_octos = surrounds_and_flashes[2]

    # increase affected octos
    for coord in adjustment_octos:
        point = new_grid[coord[0]][coord[1]]
        if point != 0:
            new_grid[coord[0]][coord[1]] += 1

    # reset flashed octos
    for coord in reset_octos:
        point = new_grid[coord[0]][coord[1]]
        if point >= 9:
            new_grid[coord[0]][coord[1]] = 0

    if new_grid != current_grid:
        new_grid = check_flashes(new_grid)

    return new_grid


grid = create_grid(formatted_data)

for _ in range(100):
    grid = add_one(grid)
    grid = check_flashes(grid)

print("Last Grid ", "-" * 50)
pprint(grid)
print("-" * 60)

print(f"flashes = {str(flashes)}")
