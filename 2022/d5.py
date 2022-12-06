#!/usr/bin/env python3

import copy
import fileinput
from typing import Tuple
import numpy as np


def get_top_of_stacks(stacks: list) -> str:
    return "".join([i[-1] for i in stacks])


def solve(commands: list, stacks: list) -> Tuple[str, str]:
    p1_stacks = copy.deepcopy(stacks)
    p2_stacks = copy.deepcopy(stacks)

    for c in commands:
        _, amount, _, src, _, dest = c.split()
        src = int(src) - 1
        dest = int(dest) - 1

        items = []
        for _ in range(int(amount)):
            p1_stacks[dest].append(p1_stacks[src].pop())
            items.append(p2_stacks[src].pop())
        p2_stacks[dest] += items[::-1]

    return get_top_of_stacks(p1_stacks), get_top_of_stacks(p2_stacks)


def parse_input(data: list) -> Tuple[list, list]:
    stack_rows, commands = "".join(data).split("\n\n")
    stack_rows = np.transpose([line[1::4] for line in stack_rows.split("\n")[:-1]])
    commands = [c.strip() for c in commands.split("\n") if c != ""]
    stacks = [[] for _ in range(len(stack_rows[0]))]

    for l in stack_rows:
        for i in range(len(l)):
            if l[i] != " ":
                stacks[i].append(l[i])

    return commands, [s[::-1] for s in stacks]


if __name__ == '__main__':
    day_input = [l for l in fileinput.input()]
    p1, p2 = solve(*parse_input(day_input))

    assert p1 == "JCMHLVGMG"
    assert p2 == "LVMRWSSPZ"
    print("p1:", p1, "p2:", p2)
