#!/usr/bin/env python

import fileinput


def perform_move(move: str, x: int, y: int) -> tuple:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    return x, y


def part_one(data: str) -> int:
    x = y = 0
    locations = [(x, y)]
    for move in data:
        x, y = perform_move(move, x, y)
        if (x, y) not in locations:
            locations.append((x, y))
    return len(locations)


def part_two(data: str) -> int:
    x1 = y1 = x2 = y2 = 0
    locations = [(x1, y1)]
    first = True
    for move in data:
        if first:
            x1, y1 = perform_move(move, x1, y1)
            if (x1, y1) not in locations:
                locations.append((x1, y1))
            first = False
        else:
            x2, y2 = perform_move(move, x2, y2)
            if (x2, y2) not in locations:
                locations.append((x2, y2))
            first = True
    return len(locations)


if __name__ == '__main__':
    data = "".join(fileinput.input())

    assert part_one('>') == 2
    assert part_one('^>v<') == 4
    assert part_one('^v^v^v^v^v') == 2
    assert part_two("^v") == 3
    assert part_two('^>v<') == 3
    assert part_two('^v^v^v^v^v') == 11
    assert part_one(data) == 2081
    assert part_two(data) == 2341

    print("p1:", part_one(data))
    print("p2:", part_two(data))
