#!/usr/bin/env python

import fileinput

def compute_most_and_least_common(dat):

    bit_lists = [[] for i in range(len(dat[0]))]

    for i in range(len(bit_lists)):
        for d in dat:
            bit_lists[i].append(d[i])

    most_common = ""
    least_common = ""
    for i in bit_lists:
        if i.count("1") == i.count("0"):
            most_common += "1"
            least_common += "0"
        elif i.count("1") > i.count("0"):
            most_common += "1"
            least_common += "0"
        else:
            most_common += "0"
            least_common += "1"
    return most_common, least_common

def life_supp(dat, oxygen):

    rating = dat.copy()

    for i in range(len(dat[0])):
        if oxygen:
            bits, _ = compute_most_and_least_common(rating)
        else:
            _, bits = compute_most_and_least_common(rating)
        for num in dat:
            if num[i] != bits[i]:
                if num in rating:
                    rating.remove(num)
            if len(rating) == 1:
                return rating[0]

if __name__ == '__main__':
    data = [l.strip() for l in fileinput.input()]

    most, least = compute_most_and_least_common(data)
    p1 = int(most, 2) * int(least, 2)

    oxygen = life_supp(data, True)
    co2 = life_supp(data, False)
    p2 = int(oxygen, 2) * int(co2, 2)


    assert p1 == 2003336
    assert p2 == 1877139

    print("p1:", p1)
    print("p2:", p2)
