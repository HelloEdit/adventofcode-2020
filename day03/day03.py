from typing import List


def walk(plan: List[List[str]], right: int, down: int):
    """Walk throught the map."""
    width = len(plan[0]) - 1

    x = 0
    y = 0
    result = 0
    while y < len(plan):
        x %= width

        if plan[y][x] == "#":
            result += 1

        x += right
        y += down

    return result


def day03(plan: List[List[str]]):
    """Count all the trees encountered for the slope right 3, down 1."""
    print("1st: {}".format(walk(plan, right=3, down=1)))


def day03bis(plan: List[List[str]]):
    """Count all the trees encountered for differents slopes then calculate the product."""
    result = walk(plan, right=1, down=1) * \
        walk(plan, right=3, down=1) * \
        walk(plan, right=5, down=1) * \
        walk(plan, right=7, down=1) * \
        walk(plan, right=1, down=2)

    print("2nd: {}".format(result))


if __name__ == "__main__":
    plan = None
    with open("./day03/input.txt") as file:
        plan = [list(x) for x in file.readlines()]

    day03(plan)
    day03bis(plan)
