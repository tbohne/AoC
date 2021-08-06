#!/usr/bin/env python
import fileinput
import re

TEST = ['\"\"', '\"abc\"', '\"aaa\\\"aaa\"', '\"\\x27\"']


def part_one(lines: list) -> int:
    original = 0
    mem = 0
    for l in lines:
        original += len(l)
        mem += len(eval(l))
    return original - mem


def part_two(lines: list) -> int:
    original = 0
    encoded = 0
    for l in lines:
        original += len(l)
        encoded += len(re.escape(l)) + l.count("\"") + 2
    return encoded - original


if __name__ == '__main__':
    assert part_one(TEST) == 12
    assert part_two(TEST) == 19
    data = [l.strip() for l in fileinput.input()]
    p1 = part_one(data)
    p2 = part_two(data)
    assert p1 == 1342
    assert p2 == 2074
    print("p1:", p1)
    print("p2:", p2)
