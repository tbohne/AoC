#!/usr/bin/python3


def part_two(data: list) -> int:
    ans = 0
    for group in data:
        for c in set(group.replace('\n', '')):
            if all([c in answer for answer in group.split('\n') if answer != '']):
                ans += 1
    return ans


def part_one(data: list) -> int:
    ans = 0
    for group in data:
        ans += len(set(group.replace('\n', '')))
    return ans


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = file.read().split('\n\n')

    assert part_one(data) == 6551
    assert part_two(data) == 3358

    print('p1:', part_one(data))
    print('p2:', part_two(data))
