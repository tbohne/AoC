#!/usr/bin/env python3

import fileinput
from typing import Tuple

DIRS = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}


def touching(h: list, t: list) -> bool:
    return h == t or t[0] == h[0] + 1 and t[1] == h[1] or t[0] == h[0] + 1 and t[1] == h[1] - 1 \
           or t[0] == h[0] + 1 and t[1] == h[1] + 1 or t[0] == h[0] and t[1] == h[1] + 1 \
           or t[0] == h[0] and t[1] == h[1] - 1 or t[0] == h[0] - 1 and t[1] == h[1] \
           or t[0] == h[0] - 1 and t[1] == h[1] + 1 or t[0] == h[0] - 1 and t[1] == h[1] - 1


def update_tails(positions: list) -> None:
    for i in range(len(positions) - 1):
        h = positions[i]
        t = positions[i + 1]
        if not touching(h, t):
            if h[0] != t[0]:
                t[0] = t[0] + 1 if h[0] > t[0] else t[0] - 1
            if h[1] != t[1]:
                t[1] = t[1] - 1 if h[1] < t[1] else t[1] + 1


def solve(data: list) -> Tuple[int, int]:
    pos = [[0, 0] for _ in range(10)]
    tail_positions_p1 = [pos[0].copy()]
    tail_positions_p2 = [pos[0].copy()]

    for direction, cnt in data:
        for _ in range(int(cnt)):
            pos[0] = [pos[0][0] + DIRS[direction][0], pos[0][1] + DIRS[direction][1]]
            update_tails(pos)
            if pos[1] not in tail_positions_p1:
                tail_positions_p1.append(pos[1].copy())
            if pos[-1] not in tail_positions_p2:
                tail_positions_p2.append(pos[-1].copy())

    return len(tail_positions_p1), len(tail_positions_p2)


if __name__ == '__main__':
    day_input = [l.strip().split() for l in fileinput.input()]
    p1, p2 = solve(day_input)
    assert p1 == 6026
    assert p2 == 2273
    print("p1:", p1, "p2:", p2)
