#!/usr/bin/env python3

import fileinput
from typing import Tuple


def solve(data: list) -> Tuple[int, int]:
    calories = sorted([sum(map(int, elve.split())) for elve in data])[::-1]
    return calories[0], sum(calories[:3])

if __name__ == '__main__':
    day_input = "".join(fileinput.input()).split('\n\n')
    p1, p2 = solve(day_input)

    assert p1 == 71300
    assert p2 == 209691
    print("p1:", p1, "p2:", p2)
