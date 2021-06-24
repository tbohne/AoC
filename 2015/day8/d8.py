#!/usr/bin/env python

TEST = ['\"\"', '\"abc\"', '\"aaa\\\"aaa\"', '\"\\x27\"']


def part_one(lines: list) -> int:
    code = 0
    mem = 0
    for l in lines:
        code += len(l)
        mem += len(eval(l))
    return code - mem


if __name__ == '__main__':
    assert part_one(TEST) == 12
    with open('in8.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]
        p1 = part_one(data)
        assert p1 == 1342
        print("p1:", p1)
