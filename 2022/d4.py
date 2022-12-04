#!/usr/bin/env python3

import fileinput


def fully_contains(l1: int, l2: int, u1: int, u2: int) -> bool:
    return (l1 >= l2 and u1 <= u2) or (l2 >= l1 and u2 <= u1)


def intersect(l1: int, l2: int, u1: int, u2: int) -> bool:
    return len(list(set(range(l1, u1 + 1)) & set(range(l2, u2 + 1)))) > 0


if __name__ == '__main__':
    day_input = [[int(i) for i in "-".join(l.split(",")).split("-")] for l in fileinput.input()]
    p1 = sum([fully_contains(l1, l2, u1, u2) for l1, u1, l2, u2 in day_input])
    p2 = sum([intersect(l1, l2, u1, u2) for l1, u1, l2, u2 in day_input])

    assert p1 == 602
    assert p2 == 891
    print("p1:", p1, "p2:", p2)
