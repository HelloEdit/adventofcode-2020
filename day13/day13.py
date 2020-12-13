from typing import List
import math


def day13(timestamp: int, ids: List[str]):
    """"""
    closest = [None, +math.inf]

    for bus in ids:
        if bus == "x":
            continue
        else:
            bus = int(bus)

        diff = bus - timestamp % bus

        if diff < closest[1]:
            closest[1] = diff
            closest[0] = bus

    print(f"1st: {closest[0] * closest[1]}")


day13bis(timestamp: int, ids: List[str]):
    pass

if __name__ == "__main__":
    timestamp = None
    ids = None
    with open("./day13/input.txt") as file:
        reading = file.readlines()

        timestamp = int(reading[0])
        ids = reading[1].split(",")

    day13(timestamp, ids)
