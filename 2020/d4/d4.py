#!/usr/bin/python3

import re

def check_val(key: str, val: str) -> bool:
    if key == 'byr':
        return re.match(r'[0-9]{4}', val) and 1920 <= int(val) <= 2002
    elif key == 'iyr':
        return re.match(r'[0-9]{4}', val) and 2010 <= int(val) <= 2020
    elif key == 'eyr':
        return re.match(r'[0-9]{4}', val) and 2020 <= int(val) <= 2030
    elif key == 'hgt':
        if re.match(r'[0-9]+cm', val):
            return 150 <= int(val.replace('cm', '')) <= 193
        elif re.match(r'[0-9]+in', val):
            return 59 <= int(val.replace('in', '')) <= 76
    elif key == 'hcl':
        return re.match(r'#[0-9a-f]{6}', val)
    elif key == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.match(r'^[0]*[0-9]{9}$', val)
    elif key == 'cid':
        return True
    return False


def has_req_fields(passport: str) -> bool:
    return all(check in passport for check in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def part_two(data: list) -> int:
    cnt = 0
    for passport in data:
        if has_req_fields(passport):
            if all(check_val(*field.split(':')) for field in passport.split(' ')):
                cnt += 1         
    return cnt


def part_one(data: list) -> int:
    return sum([has_req_fields(passport) for passport in data])


if __name__ == '__main__':

    with open('in.txt', 'r') as file:
        data = [passport.replace('\n', ' ').strip() for passport in file.read().split('\n\n')]

    assert part_one(data) == 235
    assert part_two(data) == 194

    print('p1:', part_one(data))
    print('p2:', part_two(data))
