# -*- coding: utf-8 -*-

from bisect import bisect
from collections import deque

from world.time_exception import TimeException
import timeit

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

        if time <= self.time:
            raise TimeException("Action time below World time (%s < %s)" % (time, self.time))

        if not self.schedule_list.has_key(time):
            self.schedule_list[time] = set()
        self.schedule_list[time].add(entity)


    def Schedule(self, start, stop):
        while self.times and start <= self.times[0] < stop:
            self.time = self.times.pop(0)

            for entity in self.schedule_list[self.time]:
                self.ExecuteAction(entity)

            del self.schedule_list[self.time]

    #timeit.timeit
    def ExecuteAction(self, entity):
        action = entity.GetAction(self.time)
        if action:
            action.Stop(self.time)

        action = entity.GetNextAction(self.time)
        if action:
            action.Start(self.time)
            entity.SetAction(self.time, action)
            self.AddAction(action.stop, entity)
        else:
            entity.world_entity.Kill(self.time)
