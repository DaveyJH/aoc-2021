# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4/input

with open("input-data/advent-4.txt", "r") as f:
    data = f.readlines()


numbers = [int(i) for i in data[0].rstrip("\n").split(",")]
data = data[2:]

new_data = []
for val in data:
    new_val = val.rstrip("\n")
    new_data.append(new_val)

board = []
boards = []
formatted_boards = []

for line in new_data:
    if line == "":
        boards.append(board)
        board = []
    else:
        board.append(line)
boards.append(board)

for board in boards:
    new_board = []
    for line in board:
        line = line.split()
        line = [int(i) for i in line]
        new_board.append(line)
    formatted_boards.append(new_board)


class Board():

    def __init__(self, board: list) -> None:
        self.board_data = board
        self.row_a = board[0]
        self.row_b = board[1]
        self.row_c = board[2]
        self.row_d = board[3]
        self.row_e = board[4]
        self.col_a = [
            self.row_a[0],
            self.row_b[0],
            self.row_c[0],
            self.row_d[0],
            self.row_e[0]
        ]
        self.col_b = [
            self.row_a[1],
            self.row_b[1],
            self.row_c[1],
            self.row_d[1],
            self.row_e[1]
        ]
        self.col_c = [
            self.row_a[2],
            self.row_b[2],
            self.row_c[2],
            self.row_d[2],
            self.row_e[2]
        ]
        self.col_d = [
            self.row_a[3],
            self.row_b[3],
            self.row_c[3],
            self.row_d[3],
            self.row_e[3]
        ]
        self.col_e = [
            self.row_a[4],
            self.row_b[4],
            self.row_c[4],
            self.row_d[4],
            self.row_e[4]
        ]
        self.winning_rows = [
            self.row_a,
            self.row_b,
            self.row_c,
            self.row_d,
            self.row_e,
            self.col_a,
            self.col_b,
            self.col_c,
            self.col_d,
            self.col_e,
        ]
        self.done = False

win_board_list = []
for board in formatted_boards:
    win_board_list.append(Board(board))

calls = []

def check_first_win():

    for i in range(len(numbers)):
        calls.append(numbers[i])
        for board in win_board_list:
            if not board.done:
                for line in board.winning_rows:
                    if numbers[i] in line:
                        line.remove(numbers[i])
                        if len(line) == 0:
                            board.done = True
                            return board


def check_last_win(first_board):

    finished_boards = []
    finished_boards.append(first_board)

    print(len(win_board_list))

    for i in range(len(numbers)):
        print(len(finished_boards))
        if len(finished_boards) < len(win_board_list):
            calls.append(numbers[i])
            for board in win_board_list:
                if not board.done:
                    for line in board.winning_rows:
                        if numbers[i] in line:
                            line.remove(numbers[i])
                            if len(line) == 0:
                                board.done = True
                                finished_boards.append(board)
    return finished_boards



first_win = check_first_win()
last_call = calls[-1]

total = 0
for i in first_win.board_data:
    for j in i:
        total += j

print(total * last_call)

# part two

calls = []
win_list = check_last_win(first_win)
very_last_call = calls[-1]

print(len(win_list))
print(len(numbers))

losing_total = 0
for i in win_list[-1].board_data:
    for j in i:
        losing_total += j

print(very_last_call * losing_total)
