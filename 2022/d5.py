#!/usr/bin/env python3

import copy
import fileinput
from typing import Tuple


def get_top_of_stacks(stacks: list) -> str:
    return "".join([i[-1] for i in stacks]).replace("[", "").replace("]", "")


def solve(commands: list, stacks: list) -> Tuple[int, int]:
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
    lines = []
    commands = []

    for l in data:
        if 'move' in l:
            commands.append(l.strip())
        else:
            lines.append(
                l.replace("]        ", "] [*] [*]").replace("    [", "[*] [").replace("]    ", "] [*]").strip().split())

    stacks = [[] for _ in range(len(lines[0]))]
    for l in lines[:-2]:
        for i in range(len(l)):
            if l[i] != "[*]":
                stacks[i].append(l[i])

    return commands, [s[::-1] for s in stacks]


if __name__ == '__main__':
    day_input = [l for l in fileinput.input()]
    p1, p2 = solve(*parse_input(day_input))

    assert p1 == "JCMHLVGMG"
    assert p2 == "LVMRWSSPZ"
    print("p1:", p1, "p2:", p2)
