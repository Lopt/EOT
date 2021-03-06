# -*- coding: utf-8 -*-

from bisect import bisect
import sys
from world.time_exception import TimeException
from logic.base.rand import Random

class Scheduler():
    instance = None

    def __init__(self):
        Scheduler.instance = self

        self.schedule_list = {}
        self.times         = []
        self.time          = 0

    def CreateEntity(self, type, entropy, *args, **kwargs):
        entity = type(self.time, entropy, *args, **kwargs)
        self.ExecuteAction(entity)

    def RemoveAction(self, time, entity):
        self.schedule_list[time].discard(entity)

    def AddAction(self, time, entity):
        #if time >= sys.maxint:
        #    return
        if time <= self.time:
            raise TimeException("Action time below World time (%s <= %s)" % (time, self.time))

        if time not in self.times:
            index = bisect(self.times, time)
            self.times.insert(index, time)

        if not self.schedule_list.has_key(time):
            self.schedule_list[time] = set()
        self.schedule_list[time].add(entity)

    def Schedule(self, start, stop):
        while self.times and start <= self.times[0] < stop:
            self.time = self.times.pop(0)
            while self.schedule_list[self.time]:
                entity = self.schedule_list[self.time].pop()
                self.ExecuteAction(entity)

            if not self.schedule_list[self.time]:
                del self.schedule_list[self.time]

    def ExecuteAction(self, entity):
        action = entity.GetNextAction(self.time)
        if action:
            entity.SetAction(self.time, action)
        else:
            entity.world_entity.Kill(self.time)
