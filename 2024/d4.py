#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
    grid = [i.strip() for i in fileinput.input()]
    TARGET = "XMAS"

    p1 = 0
    p2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j + 3 < len(grid[i]):  # row or reversed
                row_str = grid[i][j:j + 4]
                if row_str == TARGET or row_str[::-1] == TARGET:
                    p1 += 1
            if i + 3 < len(grid):  # col or reversed
                col_str = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
                if col_str == TARGET or col_str[::-1] == TARGET:
                    p1 += 1
            if i + 3 < len(grid) and j + 3 < len(grid[i]):  # diag or reversed (low-up)
                dl = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]
                if dl == TARGET or dl[::-1] == TARGET:
                    p1 += 1
            if i + 3 < len(grid) and j - 3 >= 0:  # diag or reversed (up-low)
                du = grid[i][j] + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3]
                if du == TARGET or du[::-1] == TARGET:
                    p1 += 1
            if grid[i][j] == "A" and i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(grid) and j + 1 < len(grid[i]):
                dl = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
                du = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]
                if (dl == TARGET[1:] or dl[::-1] == TARGET[1:]) and (du == TARGET[1:] or du[::-1] == TARGET[1:]):
                    p2 += 1
    assert p1 == 2551
    assert p2 == 1985
