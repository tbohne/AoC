#!/usr/bin/env python3

import fileinput
from typing import Tuple


def tick(cycle_register: list, crt: list) -> int:
    cycle_register[0] += 1
    register_mod = cycle_register[1] % 40 + 1
    crt_cycle_mod = (cycle_register[0] - 1) % 40 + 1

    if crt_cycle_mod in [register_mod - 1, register_mod, register_mod + 1]:
        crt[(cycle_register[0] - 1) // 40][crt_cycle_mod - 1] = "#"

    if (cycle_register[0] - 20) % 40 == 0:
        return cycle_register[0] * cycle_register[1]
    return 0


def solve(data: list) -> Tuple[int, str]:
    cycle_register = [0, 1]
    signal_strength_sum = 0
    crt = [["." for _ in range(40)] for _ in range(6)]
    for l in data:
        if len(l) == 1:
            signal_strength_sum += tick(cycle_register, crt)
        else:
            signal_strength_sum += tick(cycle_register, crt)
            signal_strength_sum += tick(cycle_register, crt)
            cycle_register[1] += int(l[1])
    return signal_strength_sum, "\n".join([" ".join(crt[i]) for i in range(6)])


if __name__ == '__main__':
    day_input = [l.strip().split() for l in fileinput.input()]
    p1, p2 = solve(day_input)
    assert p1 == 13520
    print("p1:", p1)
    print("p2:\n", p2)
