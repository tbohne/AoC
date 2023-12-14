#!/usr/bin/env python3

import fileinput

def p1(day_in):
    digits = [[c for c in code if c.isdigit()] for code in day_in]
    return sum([int(d[0] + d[-1]) for d in digits])

def p2(day_input):
    digit_str = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
    for i in range(len(day_in)):
        for k in digit_str.keys():
            if k in day_input[i]:
                day_input[i] = day_input[i].replace(k, k[0] + str(digit_str[k]) + k[-1])

    return p1(day_input)



if __name__ == '__main__':
    day_in = list(fileinput.input())
    assert p1(day_in) == 54632
    assert p2(day_in) == 54019
