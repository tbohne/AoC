#!/usr/bin/env python

import numpy as np
import math
import itertools

TEST = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]


def create_city_dict(data):
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


def create_distances(data, city_dict):
    dist = np.empty((len(city_dict), len(city_dict)))
    for l in data:
        c1, _, c2, _, d = l.split(" ")
        dist[city_dict[c1]][city_dict[c2]] = d
        dist[city_dict[c2]][city_dict[c1]] = d
    return dist


def solve(data):
    city_dict = create_city_dict(data)
    dist = create_distances(data, city_dict)
    shortest = math.inf
    longest = -math.inf
    for perm in list(itertools.permutations(city_dict.keys())):
        d = 0
        for loc in range(len(perm) - 1):
            d += dist[city_dict[perm[loc]]][city_dict[perm[loc + 1]]]
        if d < shortest:
            shortest = d
        if d > longest:
            longest = d
    return shortest, longest


if __name__ == '__main__':
    with open('in9.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]
        assert solve(TEST)[0] == 605
        assert solve(lines)[0] == 207
        assert solve(lines)[1] == 804
        print("p1:", solve(lines)[0])
        print("p2:", solve(lines)[1])
