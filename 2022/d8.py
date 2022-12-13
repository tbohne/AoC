#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from typing import Tuple
import numpy as np

VERTICAL = ["up", "down"]
HORIZONTAL = ["left", "right"]


def check_dir(grid: list, i: int, j: int, s_range: range, visible: defaultdict, direction: str) -> int:
    score = 0
    for k in s_range:
        score += 1
        if direction in VERTICAL and grid[i][j] <= grid[k][j] \
                or direction in HORIZONTAL and grid[i][j] <= grid[i][k]:
            return score
        else:
            if direction in VERTICAL and direction in visible[(k, j)] \
                    or direction in HORIZONTAL and direction in visible[(i, k)]:
                visible[(i, j)].append(direction)
    return score


def solve(grid: list) -> Tuple[int, int]:
    visible = defaultdict(list)
    scores = {}

    for x in range(len(grid)):
        visible[(0, x)].append("up")
        visible[(len(grid) - 1, x)].append("down")
        visible[(x, 0)].append("left")
        visible[(x, len(grid) - 1)].append("right")

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            scores[(i, j)] = [
                check_dir(grid, i, j, range(i - 1, -1, -1), visible, "up"),
                check_dir(grid, i, j, range(i + 1, len(grid)), visible, "down"),
                check_dir(grid, i, j, range(j - 1, -1, -1), visible, "left"),
                check_dir(grid, i, j, range(j + 1, len(grid)), visible, "right")
            ]
    return sum([len(i) > 0 for i in visible.values()]), max([np.prod(i) for i in scores.values()])


if __name__ == '__main__':
    day_input = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(day_input)
    assert p1 == 1698
    assert p2 == 672280
    print("p1:", p1, "p2:", p2)
