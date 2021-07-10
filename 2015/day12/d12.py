#!/usr/bin/env python

import json


def print_vals(dic):
    s = 0
    if isinstance(dic, dict):
        for key in dic.keys():
            if isinstance(dic[key], dict):
                s += print_vals(dic[key])
            elif isinstance(dic[key], list):
                s += print_vals(dic[key])
            else:
                if str(dic[key]).lstrip("-").isdigit():
                    s += int(dic[key])
    elif isinstance(dic, list):
        for i in dic:
            if isinstance(i, dict):
                s += print_vals(i)
            elif isinstance(i, list):
                s += print_vals(i)
            else:
                if str(i).lstrip("-").isdigit():
                    s += int(i)
    else:
        if str(dic).lstrip("-").isdigit():
            s += int(dic)
    return s


if __name__ == '__main__':
    with open('in12.txt', 'r') as file:
        data = json.loads(file.read())
        p1 = sum([print_vals(val) for _, val in data.items()])
        assert p1 == 119433
