#!/usr/bin/env python3

import fileinput
import re
from collections import defaultdict


def part_num(g, r, c):
    for r_i in [r - 1, r, r + 1]:
        for c_i in [c - 1, c, c + 1]:
            if 0 <= r_i < len(g) and 0 <= c_i < len(g[r]) and not g[r_i][c_i].isdigit() and g[r_i][c_i] != ".":
                return True
    return False


def p1(grid):
    part_nums = defaultdict(list)
    for r in range(len(grid)):
        for match in re.finditer(r'\d+', "".join(grid[r])):
            s_i, e_i = match.span()
            for c in range(s_i, e_i):
                if part_num(grid, r, c):
                    part_nums[match.group(0)].append((r, s_i, e_i))
                    break
    return sum([int(n) * len(part_nums[n]) for n in part_nums.keys()]), part_nums


def p2(grid, part_nums):
    gear_ratios = 0
    for r in range(len(grid)):
        for c, sym in enumerate(grid[r]):
            if sym == "*":
                adjacent = [(r_i, c_i) for c_i in [c - 1, c, c + 1] for r_i in [r - 1, r, r + 1]]
                adjacent_part_nums = []
                for num in part_nums.keys():
                    for r_i, s_i, e_i in part_nums[num]:
                        for c_i in range(s_i, e_i):
                            if (r_i, c_i) in adjacent:
                                adjacent_part_nums.append(num)
                                break
                if len(adjacent_part_nums) == 2:
                    gear_ratios += int(adjacent_part_nums[0]) * int(adjacent_part_nums[1])
    return gear_ratios


if __name__ == '__main__':
    day_in = [[c for c in r.strip()] for r in list(fileinput.input())]
    p1, part_num_dict = p1(day_in)
    p2 = p2(day_in, part_num_dict)
    print("p1:", p1, "\np2:", p2)
    assert p1 == 529618
    assert p2 == 77509019
