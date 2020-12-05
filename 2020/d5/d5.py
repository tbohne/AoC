#!/usr/bin/python3

from math import ceil


def binary_search(l: int, u: int, code: str) -> int:
    for c in code:
        if c == 'F':
            u -= ceil((u - l) / 2)
        else:
            l += ceil((u - l) / 2)
    return l


def get_seat_id(seat: str) -> int:
    row = binary_search(0, 127, seat[0:7])
    col = binary_search(0, 7, seat[7:10].replace('L', 'F'))
    return row * 8 + col


def part_two(data: list) -> int:
    ids = sorted([get_seat_id(b_pass) for b_pass in data])
    for i in range(part_one(data)):
        if i not in ids and i-1 in ids and i+1 in ids:
            return i


def part_one(data: list) -> int:
    return max([get_seat_id(b_pass) for b_pass in data])


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = file.readlines()

    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820

    assert part_one(data) == 801
    assert part_two(data) == 597

    print('p1:', part_one(data))
    print('p2:', part_two(data))
