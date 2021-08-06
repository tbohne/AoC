#!/usr/bin/env python

import fileinput
from hashlib import md5


def coin_mining(secret: str, zeros: int) -> int:
    num = 0
    while True:
        res = md5(bytes(secret + str(num), 'utf-8')).hexdigest()
        if res[:zeros] == "0" * zeros:
            return num
        num += 1


if __name__ == '__main__':
    assert coin_mining("abcdef", 5) == 609043
    assert coin_mining("pqrstuv", 5) == 1048970
    assert coin_mining("ckczppom", 5) == 117946
    assert coin_mining("ckczppom", 6) == 3938038

    data = "".join(fileinput.input()).strip()
    p1 = coin_mining(data, 5)
    p2 = coin_mining(data, 6)

    assert p1 == 117946
    assert p2 == 3938038
    print("p1:", p1)
    print("p2:", p2)
