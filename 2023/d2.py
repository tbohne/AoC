#!/usr/bin/env python3

import fileinput
from functools import reduce
from operator import mul

COLORS = {"r": 12, "g": 13, "b": 14}


def feasible_game(maxima):
    for c in COLORS.keys():
        if COLORS[c] < maxima[c]:
            return False
    return True


def solve(games):
    res = 0
    imp = []
    for g in range(len(games)):
        maxima = {"r": 0, "g": 0, "b": 0}
        for s in games[g].split(":")[1].split(";"):
            for cnt, color in [s.strip().split(" ") for s in s.split(",")]:
                if int(cnt) > maxima[color[0]]:
                    maxima[color[0]] = int(cnt)
            if not feasible_game(maxima):
                imp.append(g + 1)
        res += reduce(mul, maxima.values())
    return sum([i for i in range(1, len(games) + 1) if i not in imp]), res


if __name__ == '__main__':
    day_in = list(fileinput.input())
    p1, p2 = solve(day_in)
    assert p1 == 2679
    assert p2 == 77607
