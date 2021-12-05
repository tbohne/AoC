#!/usr/bin/env python

import fileinput
import numpy as np


def fill_diagram(data, diag, p1):
    for p in data:
        x1, y1, x2, y2 = [int(i) for i in " ".join(p.split("->")).replace("   ", ",").split(",")]
        diagonals = x1 != x2 and y1 != y2

        x_step = -1 if x1 > x2 else 1
        x2 = x2 - 1 if x1 > x2 else x2 + 1
        y_step = -1 if y1 > y2 else 1
        y2 = y2 - 1 if y1 > y2 else y2 + 1

        if not diagonals:
            for x in range(x1, x2, x_step):
                for y in range(y1, y2, y_step):
                    diag[x][y] += 1
        elif not p1:
            for x, y in zip(range(x1, x2, x_step), range(y1, y2, y_step)):
                diag[x][y] += 1
    return diag


def count_overlaps(diag):
    return sum([1 for x, y in np.ndindex(diag.shape) if diag[x][y] >= 2])


if __name__ == '__main__':
    data = [l.strip() for l in fileinput.input()]
    grid = np.zeros((1000, 1000))
    p1 = count_overlaps(fill_diagram(data, np.copy(grid), True))
    p2 = count_overlaps(fill_diagram(data, np.copy(grid), False))
    assert p1 == 6841
    assert p2 == 19258
    print("p1:", p1, "p2:", p2)
