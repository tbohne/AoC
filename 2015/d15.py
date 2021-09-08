#!/usr/bin/env python
import fileinput
import itertools

LIMIT = 100
CALORIES = 500


class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def parse(line):
    name = line.split(":")[0]
    properties = line.split(":")[1].split(",")
    return name, *[int(prop.strip().split(" ")[1]) for prop in properties]


def solve(ingredients, combinations, part_one):
    res = 0
    for c in combinations:
        capacity = max(0, sum([c[i] * ingredients[i].capacity for i in range(len(c))]))
        durrablity = max(0, sum([c[i] * ingredients[i].durability for i in range(len(c))]))
        flavor = max(0, sum([c[i] * ingredients[i].flavor for i in range(len(c))]))
        texture = max(0, sum([c[i] * ingredients[i].texture for i in range(len(c))]))
        calories = max(0, sum([c[i] * ingredients[i].calories for i in range(len(c))]))
        mul = capacity * durrablity * flavor * texture
        if mul > res and (part_one or calories == CALORIES):
            res = mul
    return res


if __name__ == '__main__':
    data = [line.strip() for line in fileinput.input()]
    ingredients = []
    for d in data:
        ingredients.append(Ingredient(*parse(d)))

    nums = [i for i in range(1, LIMIT + 1)]
    combinations = [i for i in list(itertools.permutations(nums, len(ingredients))) if sum(i) == LIMIT]
    p1 = solve(ingredients, combinations, True)
    p2 = solve(ingredients, combinations, False)
    assert p1 == 18965440
    assert p2 == 15862900
    print("p1:", p1)
    print("p2:", p2)
