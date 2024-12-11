#!/usr/bin/env python3

import fileinput
import re

if __name__ == '__main__':
    day_in = "".join(list(fileinput.input()))
    p1 = sum([int(i) * int(j) for i, j in re.compile(r'mul\((\d{1,3}),(\d{1,3})\)').findall(day_in)])

    active = True
    p2 = 0
    for match in re.compile(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)').finditer(day_in):
        if match[0] == "don't()":
            active = False
        elif match[0] == "do()":
            active = True
        elif active:
            p2 += int(match[1]) * int(match[2])

    assert p1 == 164730528
    assert p2 == 70478672
