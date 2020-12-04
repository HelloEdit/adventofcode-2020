from typing import List
import re

FIELDS_REQUIRED = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def day04(passports: List[str]):
    """Count the number of passports that have all the required fields."""
    correct = 0
    for entry in passports:
        if all(field in entry for field in FIELDS_REQUIRED):
            correct += 1

    print("1st: {}".format(correct))


def day04bis(passports: List[str]):
    """Count the number of passports that have all required fields and valid values."""
    separator = re.compile(r":| ")

    correct = 0
    for entry in passports:
        entry = entry.replace("\n", " ").strip()
        fields = separator.split(entry)

        if len(fields) < 14:
            continue

        # check if all required fields are here
        if not all(required in entry for required in FIELDS_REQUIRED):
            continue

        # check fields
        check = all(check_field(fields[i], fields[i + 1])
                    for i in range(0, len(fields), 2))

        if check:
            correct += 1

    print("2nd: {}".format(correct))


def check_field(name: str, value: str):
    """Check validity of specific field."""
    hcl = re.compile("^#[0-9a-f]{6}$")

    if name == "byr":
        value = int(value)
        return value >= 1920 and value <= 2002

    elif name == "iyr":
        value = int(value)
        return value >= 2010 and value <= 2020

    elif name == "eyr":
        value = int(value)
        return value >= 2020 and value <= 2030

    elif name == "hgt":
        if value.endswith("cm"):
            value = int(value[:-2])
            return value >= 150 and value <= 193

        elif value.endswith("in"):
            value = int(value[:-2])
            return value >= 59 and value <= 76

        else:
            return False

    elif name == "hcl":
        return bool(hcl.match(value))

    elif name == "ecl":
        colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return any(value == colour for colour in colours)

    elif name == "pid":
        return len(value) == 9 and value.isdigit()

    elif name == "cid":
        return True
    else:
        return False


if __name__ == "__main__":
    passports = None
    with open("./day04/input.txt") as file:
        passports = file.read().split("\n\n")

    day04(passports)
    day04bis(passports)
