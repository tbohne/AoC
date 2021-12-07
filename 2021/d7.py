#!/usr/bin/env python

import fileinput


def comp_costs(p1, p2):
    fuel = 1
    costs = 0
    for i in range(abs(p1 - p2)):
        costs += fuel
        fuel += 1
    return costs


def solve(positions, d1):
    fuels = []
    for pos in range(min(positions), max(positions)):
        fuels.append(sum([comp_costs(pos, goal_pos) if not d1 else abs(pos - goal_pos) for goal_pos in positions]))
    return min(fuels)


if __name__ == '__main__':
    data = [int(i) for i in "".join([l.strip() for l in fileinput.input()]).split(",")]
    p1 = solve(data, True)
    assert p1 == 337833
    p2 = solve(data, False)

    assert p2 == 96678050
    print("p1:", p1, "p2:", p2)
