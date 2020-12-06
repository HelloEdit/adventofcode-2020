from collections import Counter
from typing import List


def day06(answers: List[str]):
    """For each group, count the number of questions to which anyone answered "yes"."""
    result = 0
    for answer in answers:
        result += len(Counter(answer.replace(" ", "")))

    print("1st: {}".format(result))


def day06bis(answers: List[str]):
    """For each group, count the number of questions to which everyone answered "yes"."""
    result = 0
    for group in answers:
        responses = group.strip().split(" ")

        commun = set(responses[0])
        for response in responses[1:]:
            commun.intersection_update(set(response))

        result += len(commun)

    print("2nd: {}".format(result))


if __name__ == "__main__":
    answers = None
    with open("./day06/input.txt") as file:
        answers = [x.replace("\n", " ")
                   for x in file.read().split("\n\n")]

    day06(answers)
    day06bis(answers)
