# -*- coding: utf-8 -*-

from bisect import bisect
from logic.automat.time_exception import TimeException


class Scheduler():
    instance = None

    def __init__(self):
        Scheduler.instance = self

        self.schedule_list = {}
        self.times         = []
        self.time          = -1

    def AddAction(self, time, entity):
        if time not in self.times:
            index = bisect(self.times, time)
            self.times.insert(index, time)

        if time < self.time:
            raise TimeException("Schedule Time below World.time (" + str(self.time) + ") !")

        if not self.schedule_list.has_key(time):
            self.schedule_list[time] = set()
        self.schedule_list[time].add(entity)


    def Schedule(self, time):
        index = bisect(self.times, time) - 1
        if self.time < self.times[index] <= time:

            for entity in self.schedule_list[self.times[index]]:
                self.time = self.times[index]

                entity.ExecuteAction(self.times[index])