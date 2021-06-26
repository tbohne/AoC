#!/usr/bin/env python

INPUT = "1113222113"


def solve(iteration, seq):
    res = curr = ""
    cnt = 0
    for i in seq:
        if i != curr:
            if cnt > 0:
                res += (str(cnt) + curr)
            curr = i
            cnt = 1
        else:
            cnt += 1
    res += (str(cnt) + curr)

    if iteration == 0:
        return len(seq)
    else:
        return solve(iteration - 1, res)


if __name__ == '__main__':
    p1 = solve(40, INPUT)
    p2 = solve(50, INPUT)
    assert p1 == 252594
    assert p2 == 3579328
    print("p1:", p1)
    print("p2:", p2)
