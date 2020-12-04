import re
from collections import Counter, namedtuple
from typing import Dict, List


Row = namedtuple("Policy", ["lower", "higher", "letter", "password"])
policy_regex = re.compile(
    r"^(?P<lower>\d+)-(?P<higher>\d+) (?P<letter>\w): (?P<password>\w+)$")


def day02(dataset: List[Row]):
    """Count correct password according to the policy."""
    correct = 0
    for data in dataset:
        interval = range(int(data.lower), int(data.higher) + 1)
        counter = Counter(data.password)

        if counter.get(data.letter, 0) in interval:
            correct += 1

    print("1st: {}".format(correct))


def day02bis(dataset: List[Row]):
    """Count correct password according to the 'new' policy."""
    correct = 0
    for data in dataset:
        letter = data.letter
        password = data.password
        if (password[int(data.lower) - 1] == letter) ^ (password[int(data.higher) - 1] == letter):
            correct += 1

    print("2nd: {}".format(correct))


if __name__ == "__main__":
    dataset = None
    with open("./day02/input.txt") as file:
        dataset = [Row(**policy_regex.match(x).groupdict())
                   for x in file.readlines()]

    day02(dataset)
    day02bis(dataset)
