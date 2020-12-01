from typing import List


def exo1(numbers: List[int]):
    """Find the two entries that sum to 2020 and then multiply those two numbers together."""
    for first in numbers:
        for second in numbers:
            if first + second == 2020:
                return print("1st: {}".format(first * second))


def exo1bis(numbers: List[int]):
    """Find the three entries that sum to 2020 and then multiply those three numbers together."""
    for first in numbers:
        for second in numbers:
            middle = first + second
            if middle >= 2020:
                continue

            for third in numbers:
                if middle + third == 2020:
                    return print("2nd: {}".format(first * second * third))


if __name__ == "__main__":
    numbers = None
    with open("./day01/input.txt") as file:
        numbers = [int(x) for x in file.readlines()]

    exo1(numbers)
    exo1bis(numbers)
