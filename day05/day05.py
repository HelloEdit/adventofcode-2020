import math
from typing import List, Tuple


def get_seat_position(letters: str) -> Tuple[int, int]:
    """Convert boarding pass string to a row-column position."""
    row = [0, 127]
    col = [0, 7]

    # for the row
    for i in range(0, 7):
        letter = letters[i]

        middle = math.ceil((row[1] - row[0]) / 2)

        if letter == "F":
            row[1] -= middle
        if letter == "B":
            row[0] += middle

    # for the column
    for i in range(7, 10):
        letter = letters[i]

        middle = math.ceil((col[1] - col[0]) / 2)

        if letter == "L":
            col[1] -= middle
        if letter == "R":
            col[0] += middle

    return (row[0], col[0])


def day05(seats: List[str]):
    """Search for the biggest seat ID."""
    highest = -math.inf

    for seat in seats:
        position = get_seat_position(seat)

        seatid = position[0] * 8 + position[1]
        highest = max(highest, seatid)

    print("1st: {}".format(highest))


def day05bis(seats: List[str]):
    """Search for the missing seat ID of the plane."""
    taken = set()
    for seat in seats:
        position = get_seat_position(seat)
        taken.add(position[0] * 8 + position[1])

    all = set(range(min(taken), max(taken) + 1))
    diff = all.difference(taken).pop()

    print("2nd: {}".format(diff))


if __name__ == "__main__":
    seats = None
    with open("./day05/input.txt") as file:
        seats = [x.strip() for x in file.readlines()]

    day05(seats)
    day05bis(seats)
