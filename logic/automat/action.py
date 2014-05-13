# -*- coding: utf-8 -*-

from logic.world import World
from scheduler import Scheduler

class Action():
    def __init__(self, entity, name):
        #print "Init", name
        self.name   = name
        self.start  = 0
        self.stop   = 0
        self.needed = 0
        self.entity = entity

    def Start(self, start):
        #print "Start", start
        self.start = start
        Scheduler.instance.AddAction(self.start + self.needed, self.entity)

    def Stop(self, stop):
        #print "Stop", stop
        self.stop = stop

    def InTime(self, time):
        if self.stop:
            return self.start <= time <= self.stop
        else:
            return self.start <= time <= self.start + self.needed

    def IsDone(self):
        return self.start + self.needed <= World.time

    def DoneTime(self):
        return self.start_time + self.needed_time

    def PercentageDone(self, time):
        return (float(time) - self.start) / self.needed
