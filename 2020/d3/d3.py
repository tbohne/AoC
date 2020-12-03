#!/usr/bin/python3

EXAMPLE = ['..##.......',
           '#...#...#..',
           '.#....#..#.',
           '..#.#...#.#',
           '.#...##..#.',
           '..#.##.....',
           '.#.#.#....#',
           '.#........#',
           '#.##...#...',
           '#...##....#',
           '.#..#...#.#']


def solve(data: list, slopes: list) -> int:
    res = 1
    for i, j in slopes:
        r = c = cnt = 0
        while r < len(data):
            if data[r][c % len(data[r])] == '#':
                cnt += 1
            r += i
            c += j
        res *= cnt
    return res


def part_two(data: list) -> int:
    return solve(data, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])


def part_one(data: list) -> int:
    return solve(data, [(1, 3)])


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]

    assert part_one(EXAMPLE) == 7
    assert part_two(EXAMPLE) == 336
    assert part_one(data) == 145
    assert part_two(data) == 3424528800

    print("p1:", part_one(data))
    print("p2:", part_two(data))
