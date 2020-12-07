import pprint
import re
from collections import deque
from typing import Dict, List, Set

BAG = re.compile(r"^(.*) bags contain (?!no)(.*)")
INSIDE_BAGS = re.compile(r"(\d+) ((?:\w| )*) bag")


def day07(rules: List[str]):
    """Count how many bag colors can eventually contain at least one shiny gold bag."""
    bags: Dict[str, Set[str]] = {}

    for rule in rules:
        m = BAG.match(rule)
        if m:
            bags[m.group(1)] = {x[2] for x in INSIDE_BAGS.finditer(m.group(2))}

    candidate = {'shiny gold'}

    # if we are able to loop entirely on the bags, then we have all candidates
    i = 0
    loops = 0
    while i <= len(rules):
        for (name, inside) in bags.items():
            if candidate.intersection(inside) and name not in candidate:
                candidate.add(name)

                # we reset the loop to be sure we are not missing a bag
                i = 0
                break

        i += 1
        loops += 1

    print("1st: {} (in {} loops)".format(len(candidate) - 1, loops))


def day07bis(rules: List[str]):
    """Count how many individual bags are inside the shiny gold bag."""
    bags: Dict[str, Dict[str, int]] = {}

    for rule in rules:
        m = BAG.match(rule)
        if m:
            bags[m.group(1)] = {x[2]: int(x[1])
                                for x in INSIDE_BAGS.finditer(m.group(2))}

    nested = ["shiny gold"]

    for item in nested:
        if item not in bags:
            continue

        for (key, value) in bags[item].items():
            for i in range(value):
                nested.append(key)

    print("2nd: {}".format(len(nested) - 1))


if __name__ == "__main__":
    rules = None
    with open("./day07/input.txt") as file:
        rules = file.readlines()

    day07(rules)
    day07bis(rules)
