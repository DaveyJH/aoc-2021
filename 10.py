# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/10
# https://adventofcode.com/2021/day/10/input

with open("input-data/advent-10.txt", "r") as f:
    data = f.readlines()

formatted_data = [line.rstrip("\n") for line in data]

valid_opens = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}
valid_closes = {
    "]": 57,
    ")": 3,
    "}": 1197,
    ">": 25137
}
incomplete_values = {
    "[": 2,
    "(": 1,
    "{": 3,
    "<": 4
}

error_values = []
incompletes = []

for line in formatted_data:
    openers = []
    errors = []
    for char in line:
        if char in valid_opens.keys():
            openers.append(char)
        elif char in valid_closes:
            if valid_opens[openers[-1]] != char:
                errors.append(char)
                break
            else:
                openers = openers[:-1]
    if errors:
        error_values.append(valid_closes[errors[0]])
    else:
        incompletes.append(openers[::-1])

print(sum(error_values))

scores = []

for line in incompletes:
    score = 0
    for char in line:
        score = score * 5 + incomplete_values[char]
    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
