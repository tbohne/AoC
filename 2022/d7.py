#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from typing import Tuple


def solve(data: list) -> Tuple[int, int]:
    dir_dict = defaultdict(int)
    curr_path = []

    for l in data:
        if "$" in l:
            if "cd" in l and ".." not in l:
                curr_path.append(l.split()[-1].strip())
            elif l == "$ cd ..":
                assert curr_path != "/"
                curr_path.pop()
        else:
            if l.split()[0] != "dir":
                for i in range(len(curr_path) + 1):
                    dir_dict['/'.join(curr_path[:i])] += int(l.split()[0])

    total = 70000000
    unused = total - dir_dict["/"]
    required = 30000000

    p1 = sum([dir_dict[i] for i in dir_dict if dir_dict[i] <= 100000])
    p2 = min([dir_dict[i] for i in dir_dict if unused + dir_dict[i] >= required])
    return p1, p2


if __name__ == '__main__':
    day_input = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(day_input)
    assert p1 == 1783610
    assert p2 == 4370655
    print("p1:", p1, "p2:", p2)
