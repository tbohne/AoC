#!/usr/bin/env python
import fileinput


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
    data = "".join(fileinput.input()).strip()
    p1 = solve(40, data)
    p2 = solve(50, data)
    assert p1 == 252594
    assert p2 == 3579328
    print("p1:", p1)
    print("p2:", p2)
