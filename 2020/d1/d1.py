#!/usr/bin/python3

def part_two(data: list) -> int:
    needed = {2020 - x - y: (x, y) for x in data for y in data}
    for x in data:
        if x in needed:
            y, z = needed[x]
            return x * y * z


def part_one(data: list) -> int:
    needed = [2020 - x for x in data]
    for x in data:
        if x in needed:
            return x * (2020 - x)


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = [int(x) for x in file.read().split()]

    example = [1721, 979, 366, 299, 675, 1456]
    assert part_one(example) == 514579
    assert part_two(example) == 241861950

    print("p1:", part_one(data))
    print("p2:", part_two(data))
