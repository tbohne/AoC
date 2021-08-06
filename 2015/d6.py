#!/usr/bin/env python

import fileinput

import numpy as np

ON = "turn on"
OFF = "turn off"
TOGGLE = "toggle"


def activate(col_range: tuple, row_range: tuple, matrix: np.ndarray, part_one: bool):
    for i in range(*col_range):
        for j in range(*row_range):
            if part_one:
                matrix[i][j] = 1
            else:
                matrix[i][j] += 1


def deactivate(col_range: tuple, row_range: tuple, matrix: np.ndarray, part_one: bool):
    for i in range(*col_range):
        for j in range(*row_range):
            if part_one:
                matrix[i][j] = 0
            elif matrix[i][j] > 0:
                matrix[i][j] -= 1


def toggle(col_range: tuple, row_range: tuple, matrix: np.ndarray, part_one: bool):
    for i in range(*col_range):
        for j in range(*row_range):
            if part_one:
                matrix[i][j] = 0 if matrix[i][j] == 1 else 1
            else:
                matrix[i][j] += 2


def get_ranges(prefix: str, instruction: str) -> tuple:
    row_s, col_s = instruction.split('through')[0].replace(prefix, '').split(",")
    row_e, col_e = instruction.split('through')[1].split(",")
    return (int(col_s), int(col_e) + 1), (int(row_s), int(row_e) + 1)


if __name__ == '__main__':
    data = [l for l in fileinput.input()]
    matrix_p1 = np.zeros((1000, 1000))
    matrix_p2 = np.zeros((1000, 1000))

    for line in data:
        line = line.strip()
        if ON in line:
            row_r, col_r = get_ranges(ON, line)
            activate(row_r, col_r, matrix_p1, True)
            activate(row_r, col_r, matrix_p2, False)
        elif OFF in line:
            row_r, col_r = get_ranges(OFF, line)
            deactivate(row_r, col_r, matrix_p1, True)
            deactivate(row_r, col_r, matrix_p2, False)
        elif TOGGLE in line:
            row_r, col_r = get_ranges(TOGGLE, line)
            toggle(row_r, col_r, matrix_p1, True)
            toggle(row_r, col_r, matrix_p2, False)

    p1 = np.unique(matrix_p1, return_counts=True)[1][1]
    p2 = int(np.sum(matrix_p2))

    assert p1 == 400410
    assert p2 == 15343601
    print("p1:", p1)
    print("p2:", p2)
