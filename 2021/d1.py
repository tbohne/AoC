#!/usr/bin/env python

import fileinput


def count_inc(data):
    return sum([1 for i in range(1, len(data)) if data[i - 1] < data[i]])


if __name__ == '__main__':
    data = [int(l.strip()) for l in fileinput.input()]
    p1 = count_inc(data)
    p2 = count_inc([sum(data[l: l + 3]) for l in range(len(data) - 2)])

    assert p1 == 1532
    assert p2 == 1571

    print("p1:", p1)
    print("p2:", p2)
