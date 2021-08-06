#!/usr/bin/env python
import fileinput
import json
import re


def solve(dic, part_one):
    s = 0
    if isinstance(dic, dict):
        if not part_one and "red" in str(dic.values()):
            tst = str(dic)
            for i in [m.start() for m in re.finditer("red", tst)]:
                curly_sum = tst[:i].count("{") - tst[:i].count("}")
                square_sum = tst[:i].count("[") - tst[:i].count("]")
                if curly_sum == 1 and square_sum == 0:
                    return 0
        for key in dic.keys():
            if isinstance(dic[key], dict):
                s += solve(dic[key], part_one)
            elif isinstance(dic[key], list):
                s += solve(dic[key], part_one)
            else:
                if str(dic[key]).lstrip("-").isdigit():
                    s += int(dic[key])
    elif isinstance(dic, list):
        for i in dic:
            if isinstance(i, dict):
                s += solve(i, part_one)
            elif isinstance(i, list):
                s += solve(i, part_one)
            else:
                if str(i).lstrip("-").isdigit():
                    s += int(i)
    else:
        if str(dic).lstrip("-").isdigit():
            s += int(dic)
    return s


if __name__ == '__main__':
    data = json.loads("".join(fileinput.input()))
    p1 = sum([solve(val, True) for _, val in data.items()])
    p2 = sum([solve(val, False) for _, val in data.items()])
    assert p1 == 119433
    assert p2 == 68466
    print("p1:", p1)
    print("p2:", p2)
