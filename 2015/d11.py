#!/usr/bin/env python
import fileinput


def chars_allowed(pw: list) -> bool:
    return "i" not in pw and "o" not in pw and "l" not in pw


def increasing_straight(pw: list) -> bool:
    for i in range(len(pw) - 3):
        if ord(pw[i]) + 2 == ord(pw[i + 1]) + 1 == ord(pw[i + 2]):
            return True
    return False


def two_pairs(pw: list) -> bool:
    distinct = ""
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            if pw[i] not in distinct:
                distinct += pw[i]
    return len(distinct) >= 2


def increment(pw: list) -> list:
    idx = len(pw) - 1
    wrap = True
    while wrap:
        wrap = False
        num = ord(pw[idx])
        if pw[idx] == "z":
            pw[idx] = "a"
            wrap = True
            idx -= 1
        else:
            pw[idx] = chr(num + 1)
    return pw


def solve(pw: str) -> str:
    pw = list(pw)
    while not (chars_allowed(pw) and increasing_straight(pw) and two_pairs(pw)):
        pw = increment(pw)
    return "".join(pw)


if __name__ == '__main__':
    assert solve("abcdefgh") == "abcdffaa"
    assert solve("ghijklmn") == "ghjaabcc"
    data = "".join(fileinput.input()).strip()
    p1 = solve(data)
    p2 = solve(increment(list(p1)))
    assert p1 == "hxbxxyzz"
    assert p2 == "hxcaabcc"
    print("p1:", p1)
    print("p2:", p2)
