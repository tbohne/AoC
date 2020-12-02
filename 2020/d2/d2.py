#!/usr/bin/python3

def part_two(data: list) -> int:
    cnt = 0
    for i in data:
        policy, pw = i.split(":")
        pw = pw.strip()
        pos, c = policy.split(" ")
        p1, p2 = [int(x) for x in pos.split("-")]
        if (pw[p1 - 1] == c) ^ (pw[p2 - 1] == c):
            cnt += 1
    return cnt


def part_one(data: list) -> int:
    cnt = 0
    for i in data:
        policy, pw = i.split(":")
        minmax, c = policy.split(" ")
        minimum, maximum = [int(i) for i in minmax.split("-")]
        if minimum <= pw.count(c) <= maximum:
            cnt += 1
    return cnt


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = file.readlines()

    example = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert part_one(example) == 2
    assert part_two(example) == 1

    print("p1:", part_one(data))
    print("p2:", part_two(data))
