#!/usr/bin/python3


def parse_dimensions(line: str) -> tuple:
    return tuple(map(int, line.split("x")))


def part_one(line: str) -> int:
    l, w, h = parse_dimensions(line)
    x, y, _ = sorted((l, w, h))
    return 2 * l * w + 2 * w * h + 2 * h * l + x * y


def part_two(line: str) -> int:
    x, y, z = sorted(parse_dimensions(line))
    wrap = x * 2 + y * 2
    bow = x * y * z
    return wrap + bow


if __name__ == '__main__':

    assert part_one("2x3x4") == 58
    assert part_one("1x1x10") == 43
    assert part_two("2x3x4") == 34
    assert part_two("1x1x10") == 14

    with open('in2.txt', 'r') as file:
        data = file.readlines()

    wrapping = 0
    ribbon = 0
    for line in data:
        wrapping += part_one(line.strip())
        ribbon += part_two(line.strip())

    print("part one:", wrapping)
    print("part two:", ribbon)
