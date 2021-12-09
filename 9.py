# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/9
# https://adventofcode.com/2021/day/9/input

with open("input-data/advent-9.txt", "r") as f:
    data = f.readlines()

formatted_data = []

for line in data:
    formatted_data.append(list(line.rstrip("\n")))

low_points = []


def check_if_low_point(
    row_val, digit_val, c_row, c_digit, **kwargs
):
    global formatted_data

    first_row, last_row, first_digit, last_digit = False, False, False, False

    for k in kwargs:
        if k == "fr":
            first_row = True
        if k == "lr":
            last_row = True
        if k == "fd":
            first_digit = True
        if k == "ld":
            last_digit = True

    calc_1, calc_2, calc_3, calc_4 = True, True, True, True

    if not first_digit:
        calc_1 = c_digit < c_row[digit_val - 1]
    if not last_digit:
        calc_2 = c_digit < c_row[digit_val + 1]
    if not first_row:
        calc_3 = c_digit < formatted_data[row_val - 1][digit_val]
    if not last_row:
        calc_4 = c_digit < formatted_data[row_val + 1][digit_val]

    if (
        calc_1
        and calc_2
        and calc_3
        and calc_4
    ):
        low_points.append(int(c_digit))
        return True
    return False


# part 2 function
def check_for_nine(coord):

    global formatted_data

    x, y = coord

    first_row, last_row, first_digit, last_digit = False, False, False, False

    if x == 0:
        first_row = True
    if x == len(formatted_data) - 1:
        last_row = True
    if y == 0:
        first_digit = True
    if y == len(formatted_data[0]) - 1:
        last_digit = True

    global basin

    new = False

    # up one
    if not first_row:
        if formatted_data[x - 1][y] != "9":
            if (x - 1, y) not in holder:
                holder.add((x - 1, y))
                new = True
    # down one
    if not last_row:
        if formatted_data[x + 1][y] != "9":
            if (x + 1, y) not in holder:
                holder.add((x + 1, y))
                new = True
    # left one
    if not first_digit:
        if formatted_data[x][y - 1] != "9":
            if (x, y - 1) not in holder:
                holder.add((x, y - 1))
                new = True
    # right one
    if not last_digit:
        if formatted_data[x][y + 1] != "9":
            if (x, y + 1) not in holder:
                holder.add((x, y + 1))
                new = True

    return new


basin_list = []

for i, row in enumerate(formatted_data):
    for j, digit in enumerate(row):
        if i == 0:
            if j == 0:
                low_point = check_if_low_point(
                    i, j, row, digit, fr=True, fd=True)
            elif j == len(row) - 1:
                low_point = check_if_low_point(
                    i, j, row, digit, fr=True, ld=True)
            else:
                low_point = check_if_low_point(
                    i, j, row, digit, fr=True)
        elif i == len(formatted_data) - 1:
            if j == 0:
                low_point = check_if_low_point(
                    i, j, row, digit, lr=True, fd=True)
            elif j == len(row) - 1:
                low_point = check_if_low_point(
                    i, j, row, digit, lr=True, ld=True)
            else:
                low_point = check_if_low_point(i, j, row, digit, lr=True)
        elif j == 0:
            low_point = check_if_low_point(i, j, row, digit, fd=True)
        elif j == len(row) - 1:
            low_point = check_if_low_point(i, j, row, digit, ld=True)
        else:
            low_point = check_if_low_point(i, j, row, digit)
        # part 2 additional section
        if low_point:
            basin_point = (i, j)
            basin = {basin_point, }
            while True:
                new_added = []
                holder = set(basin)
                for point in basin:
                    if check_for_nine(point):
                        new_added.append(True)
                basin = set(holder)
                if len(new_added) == 0:
                    basin_list.append(basin)
                    break
        # end of part 2 additional section

risk_levels = [x + 1 for x in low_points]

total_risk = sum(risk_levels)
print(total_risk)

# part 2
basin_lengths = []

for basin in basin_list:
    basin_lengths.append(len(basin))

basin_lengths.sort()
print(basin_lengths[-1] * basin_lengths[-2] * basin_lengths[-3])
