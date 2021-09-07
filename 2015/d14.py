#!/usr/bin/env python
import fileinput

SECONDS = 2503


class Reindeer:
    def __init__(self, name, fly_speed, fly_duration, rest_time):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_duration = fly_duration
        self.rest_time = rest_time
        self.traveled_dist = 0
        self.resting = False
        self.step_cnt = 0
        self.score = 0

    def __str__(self):
        return f'{self.name}: traveled dist: {self.traveled_dist}, score: {self.score}'

    def update_state(self):
        if self.resting:
            self.step_cnt += 1
            if self.step_cnt == self.rest_time:
                self.resting = False
                self.step_cnt = 0
        else:
            self.step_cnt += 1
            self.traveled_dist += self.fly_speed
            if self.step_cnt == self.fly_duration:
                self.resting = True
                self.step_cnt = 0

    def increase_score(self):
        self.score += 1


def parse(line):
    name = line.split(" ")[0]
    return name, *[int(i) for i in line.split(" ") if i.isnumeric()]


if __name__ == '__main__':
    data = [line.strip() for line in fileinput.input()]
    reindeer = [Reindeer(*parse(line)) for line in data]

    for _ in range(SECONDS):
        for deer in reindeer:
            deer.update_state()
        states = list(reversed(sorted(reindeer, key=lambda deer: deer.traveled_dist)))
        lead_dist = states[0].traveled_dist
        for r in states:
            if r.traveled_dist == lead_dist:
                r.increase_score()
            else:
                break

    p1 = list(reversed(sorted(reindeer, key=lambda deer: deer.traveled_dist)))[0].traveled_dist
    p2 = list(reversed(sorted(reindeer, key=lambda deer: deer.score)))[0].score
    assert p1 == 2640
    assert p2 == 1102
    print("p1:", p1)
    print("p2:", p2)
