from collections import Counter
from copy import deepcopy
from itertools import product
from typing import List


def day11(seats: List[str]):
    """Count how many seats end up occupied."""
    width = len(seats[0])
    height = len(seats)

    while True:
        updated = deepcopy(seats)

        def get(x, y):
            if x < 0 or y < 0:
                return 0

            try:
                return int(seats[x][y] == "#")
            except IndexError:
                return 0

        for (x, y) in product(range(height), range(width)):
            current = seats[x][y]

            if current == ".":
                pass

            total = get(x - 1, y - 1) + get(x - 1, y) + get(x - 1, y + 1) \
                + get(x, y - 1) + get(x, y + 1) \
                + get(x + 1, y - 1) + get(x + 1, y) + get(x + 1, y + 1)

            if current == "L" and total == 0:
                updated[x][y] = "#"

            if current == "#" and total >= 4:
                updated[x][y] = "L"

        if seats == updated:
            break

        seats = updated

    freq = dict(sum(map(Counter, seats), Counter()))
    print(f"1st: {freq['#']}")


if __name__ == "__main__":
    seats = None
    with open("./day11/input.txt") as file:
        seats = [list(x.strip()) for x in file.readlines()]

    day11(seats)
