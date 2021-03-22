import re


def is_nice_part_two(s: str) -> bool:
    repeated_pair = re.compile(r'(..).*\1')
    repeat_with_separator = re.compile(r'(.).\1')
    return not (repeated_pair.search(s) is None or repeat_with_separator.search(s) is None)


def is_nice_part_one(s: str) -> bool:
    if sum(map(s.count, 'aeiou')) < 3:
        return False
    twice_in_row = re.compile(r'(.)\1')
    if not twice_in_row.search(s) or any(f in s for f in ['ab', 'cd', 'pq', 'xy']):
        return False
    return True


if __name__ == '__main__':

    with open('in5.txt', 'r') as file:
        data = file.readlines()

    cnt_one = cnt_two = 0
    for string in data:
        cnt_one += is_nice_part_one(string)
        cnt_two += is_nice_part_two(string)

    assert cnt_one == 258
    assert cnt_two == 53

    print("p1:", cnt_one)
    print("p2:", cnt_two)
