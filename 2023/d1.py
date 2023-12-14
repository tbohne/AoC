#!/usr/bin/env python3

import fileinput


def compute_calibration_val(cal_lines):
    digits = [[c for c in line if c.isdigit()] for line in cal_lines]
    return sum([int(d[0] + d[-1]) for d in digits])


def p2(cal_lines):
    digit_str = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for i in range(len(day_in)):
        for k in digit_str.keys():
            if k in cal_lines[i]:
                cal_lines[i] = cal_lines[i].replace(k, k[0] + str(digit_str[k]) + k[-1])
    return compute_calibration_val(cal_lines)


if __name__ == '__main__':
    day_in = list(fileinput.input())
    p1 = compute_calibration_val(day_in)
    p2 = p2(day_in)
    assert p1 == 54632
    assert p2 == 54019
