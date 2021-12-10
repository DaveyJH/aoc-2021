# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4/input

from collections import Counter

with open("input-data/advent-test.txt", "r") as f:
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
        new_board.append(line.split())
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


win_boards = {}
for counter, board in enumerate(formatted_boards):
    win_boards.update({counter: Board(board)})
win_board_list = []
for i in range(len(win_boards)):
    win_board_list.append(win_boards[i])

calls = []
found = False

# i = 0

# hits = []
used_boards =[]
# trur = False

for i in range(len(numbers)):
    calls.append(numbers[i])
    for board in win_board_list:
        if not board.done:
            for line in board.winning_rows:
                if str(numbers[i]) in line:
                    line.remove(str(numbers[i]))
                    if len(line) == 0:
                        board.done = True
                        used_boards.append(board)



# print("_________________________________________")

# print(win_board_list)

# print(used_boards[-1])
# print(win_board_list[-9].winning_rows)
# flob =(
#     win_board_list[-9].winning_rows[0]+
#     win_board_list[-9].winning_rows[1]+
#     win_board_list[-9].winning_rows[2]+
#     win_board_list[-9].winning_rows[3]+
#     win_board_list[-9].winning_rows[4]+
#     win_board_list[-9].winning_rows[5]+
#     win_board_list[-9].winning_rows[6]+
#     win_board_list[-9].winning_rows[7]+
#     win_board_list[-9].winning_rows[8]+
#     win_board_list[-9].winning_rows[9]
# )
# print(set(flob))

# stud = {61, 43, 58, 41, 27, 80}

# print(sum(stud))

# print(hits)
# print(calls)

# # while not found and i < len(numbers):
# #     calls.append(str(numbers[i]))
# #     for board in win_board_list:
# #         for line in board.winning_rows:
# #             if all(elem in calls for elem in line):
# #                 print(line)
# #                 print(board)
# #                 found = True
# #     i += 1

# # print(win_board_list[16].winning_rows)

# # called = ['92', '12', '94', '64', '14', '4', '99', '71', '47', '59', '37', '73', '29', '7', '16', '32', '40', '53', '30', '76', '74', '39']

# new_calls = [92, 12, 94, 64, 14, 4, 99, 71, 47, 59, 37, 73, 29, 7, 16, 32, 40, 53, 30, 76, 74, 39, 70, 88, 55, 45, 17, 0, 24, 65, 35, 20, 63, 68, 89, 84, 33, 66, 18, 50, 38, 10, 83, 75, 67, 42, 3, 56, 82, 34, 90, 46, 87, 52, 49, 2, 21, 62, 93, 86, 25, 78, 19, 57, 77, 26, 81, 15, 23, 31, 54, 48, 98, 11, 91, 85, 60, 72, 8, 69, 6, 22, 97]


# winner = [21, 50, 88, 14, 97]

# board = [
#     21, 48, 58,  4, 31,
#     50,  6, 98, 43, 41,
#     88, 80, 24, 35, 40,
#     14, 45, 61, 10, 81,
#     97, 27, 46,  8, 20
# ]

# for i in board:
#     if i in new_calls:
#         board.remove(i)


# print(board)
# print(sum(board))

# # for i in win_board_list[16].row_a:
# #     if i in called:
# #         win_board_list[16].row_a.remove(i)

# # for i in win_board_list[16].row_b:
# #     if i in called:
# #         win_board_list[16].row_b.remove(i)

# # for i in win_board_list[16].row_c:
# #     if i in called:
# #         win_board_list[16].row_c.remove(i)

# # for i in win_board_list[16].row_d:
# #     if i in called:
# #         win_board_list[16].row_d.remove(i)

# # for i in win_board_list[16].row_e:
# #     if i in called:
# #         win_board_list[16].row_e.remove(i)


# # final_sum = win_board_list[16].row_a + win_board_list[16].row_b +  win_board_list[16].row_c + win_board_list[16].row_d + win_board_list[16].row_e

# # final_calc = [int(i) for i in final_sum]
# # print(sum(final_calc))

# # print(win_board_list[16].row_a)
# # print(win_board_list[16].row_b)
# # print(win_board_list[16].row_c)
# # print(win_board_list[16].row_d)
# # print(win_board_list[16].row_e)

# # print(946*39)