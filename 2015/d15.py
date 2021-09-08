#!/usr/bin/env python
import fileinput
import itertools

LIMIT = 100

class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return f'{self.name}: cap: {self.capacity}, dur: {self.durability}, flav: {self.flavor}, text: {self.texture}, cal: {self.calories}'


def parse(line):
    name = line.split(":")[0]
    properties = line.split(":")[1].split(",")
    return name, *[int(prop.strip().split(" ")[1]) for prop in properties]


def part_one(ingredients, combinations):
    res = 0
    for c in combinations:
        cap = max(0, sum([c[i] * ingredients[i].capacity for i in range(len(c))]))
        dur = max(0, sum([c[i] * ingredients[i].durability for i in range(len(c))]))
        flav = max(0, sum([c[i] * ingredients[i].flavor for i in range(len(c))]))
        text = max(0, sum([c[i] * ingredients[i].texture for i in range(len(c))]))
        mul = cap * dur * flav * text
        if mul > res:
            res = mul
    return res


if __name__ == '__main__':

    data = [line.strip() for line in fileinput.input()]
    ingredients = []
    for d in data:
        ingredients.append(Ingredient(*parse(d)))

    nums = [i for i in range(1, LIMIT + 1)]
    combinations = [i for i in list(itertools.permutations(nums, len(ingredients))) if sum(i) == LIMIT]
    p1 = part_one(ingredients, combinations)
    assert p1 == 18965440
    print("p1:", p1)

