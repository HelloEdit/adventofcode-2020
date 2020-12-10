from typing import List


def day10(jolts: List[int]):
    """Find the number of 1-jolt differences multiplied by these of 3-jolt."""
    rating = 0
    difference = {1: 0, 3: 1}

    for jolt in jolts:
        diff = jolt - rating
        difference[diff] += 1

        rating = jolt

    print(f"1st: {difference[1] * difference[3]}")


def day10bis(jolts: List[int]):
    """Find the number of possible arrangments."""
    # I would like to note that I was greatly helped in this part.

    p = {}
    p[0] = 1

    for jolt in jolts:
        p[jolt] = p.get(jolt - 3, 0) + p.get(jolt - 2, 0) + p.get(jolt - 1, 0)

    print(f"2nd: {p[max(jolts)]}")


if __name__ == "__main__":
    jolts = None
    with open("./day10/input.txt") as file:
        jolts = {int(x) for x in file.readlines()}

    day10(jolts)
    day10bis(jolts)
