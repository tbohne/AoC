#!/usr/bin/python3

from typing import Tuple


def parse_dimensions(line: str) -> Tuple[int, int, int]:
    l = int(line.strip().split("x")[0])
    w = int(line.strip().split("x")[1])
    h = int(line.strip().split("x")[2])
    return l, w, h


def part_one(line: str) -> int:
    l, w, h = parse_dimensions(line)
    dim = sorted((l, w, h))
    return 2 * l * w + 2 * w * h + 2 * h * l + dim[0] * dim[1]


def part_two(line: str) -> int:
    dim = sorted(parse_dimensions(line))
    wrap = dim[0] * 2 + dim[1] * 2
    bow = dim[0] * dim[1] * dim[2]
    return wrap + bow


if __name__ == '__main__':

    assert part_one("2x3x4") == 58
    assert part_one("1x1x10") == 43
    assert part_two("2x3x4") == 34
    assert part_two("1x1x10") == 14

    with open('input2.txt', 'r') as file:
        data = file.readlines()

    wrapping = 0
    ribbon = 0
    for line in data:
        wrapping += part_one(line)
        ribbon += part_two(line)

    print("part one:", wrapping)
    print("part two:", ribbon)
