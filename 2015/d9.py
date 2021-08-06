#!/usr/bin/env python

import numpy as np
import itertools
import fileinput

TEST = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]


def create_city_dict(data: list) -> dict:
    idx = 0
    idx_to_city = {}
    for l in data:
        c1, _, c2, _, _ = l.split(" ")
        if c1 not in idx_to_city:
            idx_to_city[c1] = idx
            idx += 1
        if c2 not in idx_to_city:
            idx_to_city[c2] = idx
            idx += 1
    return idx_to_city


def create_distances(data: list, city_dict: dict) -> np.array:
    dist = np.empty((len(city_dict), len(city_dict)))
    for l in data:
        c1, _, c2, _, d = l.split(" ")
        dist[city_dict[c1]][city_dict[c2]] = dist[city_dict[c2]][city_dict[c1]] = d
    return dist


def solve(data: list) -> (int, int):
    d = create_city_dict(data)
    dist = create_distances(data, d)
    permutations = list(itertools.permutations(d.keys()))
    d = [sum([dist[d[perm[loc]]][d[perm[loc + 1]]] for loc in range(len(perm) - 1)]) for perm in permutations]
    return min(d), max(d)


if __name__ == '__main__':
    assert solve(TEST)[0] == 605
    lines = [l.strip() for l in fileinput.input()]
    p1, p2 = solve(lines)
    assert p1 == 207
    assert p2 == 804
    print("p1:", p1)
    print("p2:", p2)
