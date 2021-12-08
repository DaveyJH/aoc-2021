# replace ??? with current day
# add test data to input-data/advent-test.txt
# replace test with current day when happy with script

# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6/input

with open("input-data/advent-6.txt", "r") as f:
    data = f.readlines()

formatted_data = []

separate_strings = data[0].split(",")
for string in separate_strings:
    formatted_data.append(int(string))


# part 1, slow and memory heavy
def add_fish():
    """Add a new instance of Fish to the new_results list"""

    new_results.append(Fish())


class Fish():
    """Creates a Fish

    ---
    Attributes:
        age (int): (default=8) current age of fish
        new_born (bool): (default=True) prevents reduction of age after
            intitial instantiation
    """

    def __init__(self, age=8, new_born=True):
        self.age = age
        self.new_born = new_born

    def reduce_days(self):

        if not self.new_born:
            if self.age > 0:
                self.age -= 1
            else:
                add_fish()
                self.age = 6
        else:
            self.new_born = False
        return self

    def __repr__(self):
        return f"{self.age}"


def create_fish(age):
    """Create initial data input fish with current age"""

    return Fish(age, False)


new_results = list(map(create_fish, formatted_data))

for i in range(80):
    new_results = list(map(Fish.reduce_days, new_results))
print(len(new_results))


# !WILL NOT WORK DUE TO MEMORY - RETHINK!
# for i in range(256 - 80):
#     new_results = list(map(Fish.reduce_days, new_results))
# print(len(new_results))

#######################################

# part 2, far more simple
day = {i: 0 for i in range(9)}


def calculate_fish(num_of_days):
    """Calculate the resulting number of fish"""

    # reset day to 0
    for k in day:
        day.update({k: 0})
    # assign fish from data to their current age
    for i in formatted_data:
        day[i] += 1

    # for i in range(num_of_days):
    while num_of_days > 0:
        for k, v in day.items():
            if k == 0:
                old_fish = v
            else:
                day.update({k - 1: v})
        day[8] = old_fish
        day[6] = day[6] + old_fish
        num_of_days -= 1

    num_of_fish = 0

    for v in day.values():
        num_of_fish += v

    return num_of_fish


print(calculate_fish(80))  # proof
print(calculate_fish(256))
