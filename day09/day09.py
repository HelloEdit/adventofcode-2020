from itertools import combinations
from typing import List


def day09(xmas: List[int]):
    """Find the first number in the list (after the preamble) which is not the sum of previous number."""

    def is_sum(number: int, candidates: List[int]):
        """Determine if a number can be expressed as the sum of two differents numbers."""
        for (a, b) in combinations(candidates, r=2):
            if a == b:
                continue

            if a + b == number:
                return True

        return False

    for i in range(25, len(xmas)):
        previous = xmas[i - 25:i]
        actual = xmas[i]

        if not is_sum(actual, previous):
            return actual


def day09bis(number: int, xmas: List[int]):
    """Find a contiguous set of at least two numbers then sum the min and the max."""
    start = 0
    end = 1
    total = 0

    while True:
        if total < number:
            end += 1
        elif total > number:
            start += 1
        else:
            slice = xmas[start:end]
            return print(f"2nd: {max(slice) + min(slice)}")

        total = sum(xmas[start:end])


if __name__ == "__main__":
    xmas = None
    with open("./day09/input.txt") as file:
        xmas = [int(x) for x in file.readlines()]

    number = day09(xmas)
    print(f"1st: {number}")

    day09bis(number, xmas)
