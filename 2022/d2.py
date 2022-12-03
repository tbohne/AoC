#!/usr/bin/env python3

import fileinput

WINNING_MOVES = {'A': 'B', 'B': 'C', 'C': 'A'}
LOSING_MOVES = {'A': 'C', 'B': 'A', 'C': 'B'}


def score(option: str) -> int:
    return ord(option) - 64


def solve_p1(data: list) -> int:
    s = 0
    for moves in data:
        s += score(moves[1])
        if moves[0] == moves[1]:
            s += 3
        elif WINNING_MOVES[moves[0]] == moves[1]:
            s += 6
    return s


def solve_p2(data: list) -> int:
    s = 0
    for moves in data:
        if moves[1] == 'B':
            s += score(moves[0]) + 3
        elif moves[1] == 'A':
            s += score(LOSING_MOVES[moves[0]])
        else:
            s += 6 + score(WINNING_MOVES[moves[0]])
    return s


if __name__ == '__main__':
    day_input = [l.replace('X', 'A').replace('Y', 'B').replace('Z', 'C').split() for l in fileinput.input()]
    p1 = solve_p1(day_input)
    p2 = solve_p2(day_input)

    assert p1 == 15691
    assert p2 == 12989
    print("p1:", p1, "p2:", p2)
