#!/usr/bin/env python3

import fileinput
import numpy as np


def solve(data: list, dist_cnt: int) -> int:
    for i in range(len(data) - dist_cnt):
        if len(np.unique(list(data[i: i + dist_cnt]))) == dist_cnt:
            return i + dist_cnt


if __name__ == '__main__':
    day_input = [l for l in fileinput.input()][0]
    p1 = solve(day_input, 4)
    p2 = solve(day_input, 14)

    assert p1 == 1625
    assert p2 == 2250
    print("p1:", p1, "p2:", p2)
