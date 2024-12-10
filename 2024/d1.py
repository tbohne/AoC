#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
    day_in = [i.split() for i in fileinput.input()]
    left = sorted([int(i[0]) for i in day_in])
    right = sorted([int(i[1]) for i in day_in])
    p1 = sum([abs(left[i] - right[i]) for i in range(len(left))])
    p2 = sum([i * right.count(i) for i in left])

    assert p1 == 1941353
    assert p2 == 22539317
