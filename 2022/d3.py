#!/usr/bin/env python3

import fileinput
from typing import Tuple


def priority_sum(intersections: list) -> int:
    return sum([ord(i) - 96 if i.islower() else ord(i) - 38 for i in intersections])


def solve(data: list) -> Tuple[int, int]:
    i1 = [list(set(r[:len(r) // 2]) & set(r[len(r) // 2:]))[0] for r in data]
    i2 = [list(set(data[i]) & set(data[i + 1]) & set(data[i + 2]))[0] for i in range(0, len(data) - 2, 3)]
    return priority_sum(i1), priority_sum(i2)


if __name__ == '__main__':
    day_input = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(day_input)
    assert p1 == 8394
    assert p2 == 2413
    print("p1:", p1, "p2:", p2)
