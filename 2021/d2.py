#!/usr/bin/env python

import fileinput


def solve(data):
    hori = depth_p1 = depth_p2 = aim = 0

    for i in data:
        direct, amount = i.split()
        amount = int(amount)
        if direct == "forward":
            hori += amount
            depth_p2 += aim * amount
        elif direct == "down":
            depth_p1 += amount
            aim += amount
        elif direct == "up":
            depth_p1 -= amount
            aim -= amount
    return hori * depth_p1, hori * depth_p2


if __name__ == '__main__':
    data = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(data)
    assert p1 == 2070300
    assert p2 == 2078985210
    print("p1:", p1)
    print("p2:", p2)
