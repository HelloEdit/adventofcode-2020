from typing import List

COMPASS = ["N", "E", "S", "W"]


class Boat(object):
    """Represents a boat and its position."""

    x: int = 0
    y: int = 0
    current: int = 1

    def move(self, action: str, arg: int):
        """Move the ship."""
        if action == "N":
            self.x += arg
        elif action == "S":
            self.x -= arg
        elif action == "E":
            self.y += arg
        elif action == "W":
            self.y -= arg

    def rotate(self, degrees, side):
        """Rotate the ship by a number of degrees."""
        steps = int(degrees / 90)

        if side == "R":
            self.current = (self.current + steps) % 4

        if side == "L":
            self.current = (self.current - steps) % 4

    def get_manhattan(self):
        """Get Manhattan distance between (0, 0) and the current position."""
        return abs(self.x + self.y)

    def get_orientation(self):
        """Get the current orientation of the boat."""
        return COMPASS[self.current]


def day12(orders: List[str]):
    """Calculate the Manhattan distance between (0, 0) and the last position."""
    boat = Boat()

    for order in orders:
        action, arg = order[: 1], int(order[1:])

        if action == "L" or action == "R":
            boat.rotate(arg, side=action)
            continue

        if action == "F":
            boat.move(boat.get_orientation(), arg)
            continue

        boat.move(action, arg)

    print(f"1st: {boat.get_manhattan()}")


if __name__ == "__main__":
    orders = None
    with open("./day12/input.txt") as file:
        orders = file.readlines()

    day12(orders)
