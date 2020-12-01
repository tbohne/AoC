#!/usr/bin/python3

def part_two(data: list) -> int:
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    return x * y * z
    return 0


def part_one(data: list) -> int:
    for x in data:
        for y in data:
            if x + y == 2020:
                return x * y
    return 0


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = [int(x) for x in file.read().split()]

    example = [1721, 979, 366, 299, 675, 1456]
    assert part_one(example) == 514579
    assert part_two(example) == 241861950

    print("p1:", part_one(data))
    print("p2:", part_two(data))
