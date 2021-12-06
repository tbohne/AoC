#!/usr/bin/env python

import fileinput


def solve(fishes, days):
    fish_timer = {i: fishes.count(i) for i in range(0, 9)}

    for day in range(1, days + 1):
        zero_cnt = fish_timer[0]

        for d in range(1, 9):
            fish_timer[d - 1] += fish_timer[d]
            fish_timer[d] -= fish_timer[d]

        fish_timer[0] -= zero_cnt
        fish_timer[6] += zero_cnt
        fish_timer[8] += zero_cnt

    return sum([val for val in fish_timer.values()])


if __name__ == '__main__':
    fishes = [int(i) for i in "".join([l.strip() for l in fileinput.input()]).split(",")]
    p1 = solve(fishes, 80)
    p2 = solve(fishes, 256)
    assert p1 == 380758
    assert p2 == 1710623015163
    print("p1:", p1, " p2:", p2)
