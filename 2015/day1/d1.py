#!/usr/bin/python3

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
    with open('in1.txt', 'r') as file:
        data = file.read().replace('\n', '')
    floor, first_basement = solve(data)
    print("part one:", floor)
    print("part two:", first_basement)
