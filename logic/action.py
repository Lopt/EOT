# -*- coding: utf-8 -*-

from logic.world import World
from logic.scheduler import Scheduler

class Action():

    def __init__(self, entity, action, needed_time):
        self.entity      = entity
        self.start_time  = World.time
        self.stop_time   = None
        self.needed_time = needed_time
        self.action      = action

    def InRange(self, time):
        if self.stop_time:
            return self.start_time <= time <= self.stop_time
        else:
            return self.start_time <= time <= self.start_time + self.needed_time

    def Activate(self):
        Scheduler.instance.AddAction(self.entity, self.start_time)

    def IsDone(self):
        return self.start_time + self.needed_time <= World.time

    def DoneTime(self):
        return self.start_time + self.needed_time

    def PercentageDone(self):
        return (float(World.time) - self.start_time) / self.needed_time

    def Start(self):
        self.start_time = World.time
        Scheduler.instance.AddAction(self.entity, self.DoneTime())

    def Stop(self):
        self.stop_time = World.time

    def __repr__(self):
        return "<Type: %s Time: (%i + %i)=%s Entity %s>" % (self.action, self.start_time, self.needed_time, str(self.stop_time), self.entity)
