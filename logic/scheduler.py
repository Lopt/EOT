# -*- coding: utf-8 -*-

from logic.world import World
from threading import Thread, Lock


class Scheduler():
    instance = None
    def __init__(self):
        Scheduler.instance = self
            
        self.schedule_list = {}
        self.times         = set()
        self.threads       = []

    def AddAction(self, entity, time):
        time = int(time)
        if time < World.time:
            raise Exception("Schedule Time below World.time (" + str(World.time) + ") !")

        self.times.add(time)
        if not self.schedule_list.has_key(time):
            self.schedule_list[time] = set()
        self.schedule_list[time].add(entity)

    def RemoveActiom(self, entity, time):
        if time <= World.time:
            raise Exception("Schedule Time below World.time!")
        time = int(time)
        
        if self.schedule_list.has_key(time):
            self.schedule_list[time].discard(entity)
            if not self.schedule_list[time]:
                del self.schedule_list[time]
                self.times.discard(time)


    def Schedule(self, time):
        World.time = time
        if time in self.times:
            self.times.discard(time)

            for entity in self.schedule_list[World.time]:
                entity.Action(time)