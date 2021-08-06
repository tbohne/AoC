#!/usr/bin/env python

import fileinput
from typing import Tuple


def solve(data: str) -> Tuple[int, int]:
    floor = 0
    basement = -1
    for pos, direction in enumerate(data, 1):
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -= 1
        if floor == -1 and basement == -1:
            basement = pos
    return floor, basement


if __name__ == '__main__':
    data = "".join(fileinput.input())
    floor, first_basement = solve(data)
    assert floor == 232
    assert first_basement == 1783
    print("p1:", floor)
    print("p2:", first_basement)
