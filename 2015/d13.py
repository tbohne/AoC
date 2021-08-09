#!/usr/bin/env python
import fileinput
import itertools


def preprocess_data(raw_data):
    dic = {}
    for l in raw_data:
        name, _, mode, amount, _, _, _, _, _, _, partner = l.split(" ")
        dic[(name, partner.replace(".", ""))] = int(amount) if mode == "gain" else -int(amount)
    res = {}
    name_list = []
    for key in dic.keys():
        n1, n2 = key
        if n1 not in name_list:
            name_list.append(n1)
        if (n2, n1) not in res.keys():
            res[key] = dic[key] + dic[(n2, n1)]
    return res, name_list


def compute_optimal_happiness_change(info, names, part_one):
    if not part_one:
        names.append("ME")
    optimal_change = 0
    for perm in list(itertools.permutations(names)):
        change = 0
        for i in range(len(perm) - 1):
            if (perm[i], perm[i + 1]) in info.keys():
                change += info[perm[i], perm[i + 1]]
            else:
                if part_one or perm[i] != "ME" and perm[i + 1] != "ME":
                    change += info[perm[i + 1], perm[i]]

        if (perm[0], perm[len(perm) - 1]) in info:
            change += info[perm[0], perm[len(perm) - 1]]
        else:
            if part_one or perm[0] != "ME" and perm[len(perm) - 1] != "ME":
                change += info[perm[len(perm) - 1], perm[0]]
        if change >= optimal_change:
            optimal_change = change
    return optimal_change


if __name__ == '__main__':
    data = [l.strip() for l in fileinput.input()]
    data, names = preprocess_data(data)
    p1 = compute_optimal_happiness_change(data, names, True)
    p2 = compute_optimal_happiness_change(data, names, False)
    assert p1 == 709
    assert p2 == 668
    print("p1:", p1)
    print("p2:", p2)
