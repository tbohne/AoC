#!/usr/bin/env python

import numpy as np
import math
import itertools

TEST = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]


def create_city_dict(data):
    idx = 0
    idx_to_city = {}
    for l in data:
        c1 = l.split(" ")[0]
        c2 = l.split(" ")[2]
        if not c1 in idx_to_city:
            idx_to_city[c1] = idx
            idx += 1
        if not c2 in idx_to_city:
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


def part_one(data):
    city_dict = create_city_dict(data)
    dist = create_distances(data, city_dict)
    shortest = math.inf
    for perm in list(itertools.permutations(city_dict.keys())):
        d = 0
        for loc in range(len(perm) - 1):
            d += dist[city_dict[perm[loc]]][city_dict[perm[loc + 1]]]
        if d < shortest:
            shortest = d
    return shortest


if __name__ == '__main__':
    with open('in9.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]
        assert part_one(TEST) == 605
        assert part_one(data) == 207
        print("p1:", part_one(data))

