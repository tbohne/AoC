#!/usr/bin/env python3

import fileinput
from typing import List


def check_pages(rule_tuples: List[List[str]], pages: List[str]) -> List[int]:
    violations = []
    for i, r in enumerate(rule_tuples):
        if r[0] in pages and r[1] in pages and pages.index(r[0]) > pages.index(r[1]):
            violations.append(i)
    return violations


def fix_violation(v: int, p: List[str]) -> List[str]:
    a = p.index(rule_tuples[v][0])
    b = p.index(rule_tuples[v][1])
    return p[:b] + [p.pop(a)] + p[b:]


if __name__ == '__main__':
    day_in = [i.strip() for i in fileinput.input()]
    rule_tuples = [l.split("|") for l in day_in if "|" in l]
    pages = [l.split(",") for l in day_in if "," in l]

    p1 = 0
    p2 = 0
    for p in pages:
        violations = check_pages(rule_tuples, p)
        if len(violations) == 0:
            p1 += int(p[len(p) // 2])
        else:
            while len(violations) > 0:
                p = fix_violation(violations[0], p)
                violations = check_pages(rule_tuples, p)
            p2 += int(p[len(p) // 2])
    assert p1 == 5762
    assert p2 == 4130
