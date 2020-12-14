import re
from typing import Dict, List

MEM_RE = re.compile(r"^mem\[(\d+)\] = (\d+)$")


def compute(mask):
    """Compute the mask to a tuple position-value."""
    return [(len(mask) - i - 1, int(c)) for (i, c) in enumerate(mask) if c.isdigit()]


def set_bit(value, bit):
    """Set specific bit to 0."""
    return value | (1 << bit)


def clear_bit(value, bit):
    """Set specific bit to 1."""
    return value & ~(1 << bit)


def day14(chunks: List[str]):
    """Run then initialization program."""
    memory: Dict[int, int] = {}

    mask = None
    for chunk in chunks:
        if chunk.startswith("mask ="):
            mask = compute(chunk.split("= ")[1].strip())
            continue

        match = MEM_RE.match(chunk)
        adr, val = int(match.group(1)), int(match.group(2))

        for (p, b) in mask:
            if b == 1:
                val = set_bit(val, p)
            elif b == 0:
                val = clear_bit(val, p)

        memory.update({adr: val})

    print(f"1st: {sum(memory.values())}")


if __name__ == "__main__":
    chunks = None

    with open("./day14/input.txt") as file:
        chunks = file.readlines()

    day14(chunks)
