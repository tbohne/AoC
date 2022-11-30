#!/usr/bin/env python

import fileinput


def solve(data, sec):
    coords = [0, 0]
    # [east, south, west, north]
    directions = [(0, 1), (1, -1), (0, -1), (1, 1)]
    dir_idx = 3  # starting north
    list_of_coords = [coords.copy()]

    for cmd in data:
        if cmd[0] == 'R':
            dir_idx = (dir_idx + 1) % len(directions)
        elif cmd[0] == 'L':
            dir_idx = (dir_idx - 1) % len(directions)

        for _ in range(int(cmd[1:])):
            coords[directions[dir_idx][0]] += directions[dir_idx][1]
            if sec and coords in list_of_coords:
                return sum([abs(c) for c in coords])
            list_of_coords.append(coords.copy())

    return sum([abs(c) for c in coords])


if __name__ == '__main__':
    data = [i.strip() for i in [l for l in fileinput.input()][0].split(",")]
    p1 = solve(data, False)
    p2 = solve(data, True)

    assert p1 == 241
    assert p2 == 116
