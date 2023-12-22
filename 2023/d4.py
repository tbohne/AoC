#!/usr/bin/env python3

import fileinput


def p1(cards):
    cd = {}
    for idx, l in enumerate(cards):
        card, my = l.split("|")
        card = [int(i) for i in card.split(":")[1].split(" ") if i != ""]
        my = [int(i) for i in my.split(" ") if i != ""]
        cd[idx + 1] = (card, my, 1, len([i for i in my if i in card]))
    return sum([2 ** (cd[k][3] - 1) if cd[k][3] > 0 else 0 for k in cd.keys()]), cd


def p2(cd):
    for k in cd.keys():
        for _ in range(cd[k][2]):
            for i in range(k + 1, k + cd[k][3] + 1):
                cd[i] = (cd[i][0], cd[i][1], cd[i][2] + 1, cd[i][3])
    return sum([cd[k][2] for k in cd.keys()])


if __name__ == '__main__':
    day_in = list(fileinput.input())
    p1, card_dict = p1(day_in)
    p2 = p2(card_dict)
    assert p1 == 27845
    assert p2 == 9496801
