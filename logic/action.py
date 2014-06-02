# -*- coding: utf-8 -*-
from logic.scheduler import Scheduler

from world.action import DefaultAction
import sys

class Action():
    counter = 0

    def __init__(self, entity, *args, **kwargs):
        self.entity = entity
        self.world_action = DefaultAction
        self.start = 0
        self.needed = sys.maxint
        self.OnInit(*args, **kwargs)

    def Start(self, time):
        self.start = time
        self.OnStart(time)

        self.entity.world_entity.AddAction(time, self.world_action)
        Scheduler.instance.AddAction(self.DoneTime(), self.entity)

    def Stop(self, time):
        self.OnStop(time)
        Scheduler.instance.RemoveAction(self.DoneTime(), self.entity)
        self.entity = None

    def IsDone(self, time):
        return time >= self.start + self.needed

    def DoneTime(self):
        return self.start + self.needed

    # returns a list of (other) actions which should come in front of it (as example, before you chop a tree, walk to it)
    def BeforeStart(self):
        return []

    def OnInit(self, *args, **kwargs):
        pass

    def OnStart(self, time):
        pass

    def OnStop(self, time):
        pass