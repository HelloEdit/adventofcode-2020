from typing import List


def execute(code: List[str]):
    """Run a copy of the boot."""
    seen = set()
    acc = 0

    i = 0
    while i < len(code):
        if i in seen:
            return (False, acc)
        else:
            seen.add(i)

        [reg, arg] = code[i].split(" ")

        if reg == "jmp":
            i += int(arg)
            continue

        elif reg == "acc":
            acc += int(arg)

        elif reg == "nop":
            pass

        i += 1

    return (True, acc)


def day08(code: List[str]):
    """Calculate the value in accumulator before looping."""
    (_, acc) = execute(code)

    print("1st: {}".format(acc))


def day08bis(code: List[str]):
    """Fix the program by by trying out all the possibilities."""

    # this is ugly and I apologize
    for (index, line) in enumerate(code):
        copy = code[:]

        [reg, arg] = line.split(" ")

        if reg == "jmp":
            reg = "nop"
        elif reg == "nop":
            reg = "jmp"
        else:
            continue

        copy[index] = ' '.join([reg, arg])

        (eof, acc) = execute(copy)
        if eof:
            return print("2nd: {}".format(acc))


if __name__ == "__main__":
    code = None
    with open("./day08/input.txt") as file:
        code = [line.strip() for line in file.readlines()]

    day08(code)
    day08bis(code)
