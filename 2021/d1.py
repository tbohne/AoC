#!/usr/bin/env python

import fileinput


def solve(data, win_size):
    num = None
    cnt = 0

    for l in range(len(data) - win_size + (win_size > 0)):
        s = sum(data[l: l + win_size + (win_size == 0)])
        if num is not None and s > num:
            cnt += 1
        num = s
    return cnt


if __name__ == '__main__':
    data = [int(l.strip()) for l in fileinput.input()]
    p1 = solve(data, 0)
    p2 = solve(data, 3)

    assert p1 == 1532
    assert p2 == 1571

    print("p1:", p1)
    print("p2:", p2)
