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

    def __str__(self):
        return f'{self.name}: speed ({self.fly_speed}), fly duration: ({self.fly_duration}), rest time: ({self.rest_time}, current travel dist: ({self.traveled_dist}))'

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


def parse(line):
    name = line.split(" ")[0]
    return name, *[int(i) for i in line.split(" ") if i.isnumeric()]


if __name__ == '__main__':
    data = [line.strip() for line in fileinput.input()]
    reindeer = []
    for l in data:
        reindeer.append(Reindeer(*parse(l)))

    for i in range(SECONDS):
        for deer in reindeer:
            deer.update_state()

    winner = list(reversed(sorted(reindeer, key=lambda deer: deer.traveled_dist)))[0]
    p1 = winner.traveled_dist
    assert p1 == 2640
    print("p1:", p1)
