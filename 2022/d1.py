#!/usr/bin/env python3

import fileinput
from typing import Tuple


def solve(data: list) -> Tuple[int, int]:
    elves = [[]]
    for calories in data:
        if calories:
            elves[-1].append(int(calories))
        else:
            elves.append([])
    return max([sum(i) for i in elves]), sum(sorted(sum(i) for i in elves)[::-1][:3])


if __name__ == '__main__':
    day_input = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(day_input)

    assert p1 == 71300
    assert p2 == 209691
    print("p1:", p1, "p2:", p2)
