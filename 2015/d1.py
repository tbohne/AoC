#!/usr/bin/python3

from typing import Optional, Tuple


def solve(data: str) -> Tuple[int, Optional[int]]:
    floor = 0
    basement = None
    for pos, direction in enumerate(data, 1):
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -= 1
        if floor == -1 and basement is None:
            basement = pos
    return floor, basement


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    floor, first_basement = solve(data)
    print("part one:", floor)
    print("part two:", first_basement)
