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
            
        self.temp  = []            
            
    def AddEntity(self, entity):
        World.entities.append(entity)
        self.AddToSchedule(entity, World.time)
        
    def RemoveEntity(self, entity):
        if entity.actions:
            self.RemoveFromSchedule(entity, entity.actions[-1].DoneTime())
        World.entities.remove(entity)
    
    def AddToSchedule(self, entity, time):
        if time < World.time: 
            raise Exception("Schedule Time below World.time!")
        time = int(time)        
        self.times.add(time)        
        
        if not self.schedule_list.has_key(time):
            self.schedule_list[time] = []
        self.schedule_list[time].append(entity)
    
    def RemoveFromSchedule(self, entity, time):
        if time < World.time: 
            raise Exception("Schedule Time below World.time!")
        time = int(time)        
        
        if self.schedule_list.has_key(time):
            self.schedule_list[time].remove(entity)
            if not self.schedule_list[time]:
                del self.schedule_list[time]
                self.times.discard(time)
    
    
    def Schedule(self, time):
        World.time = time   
        
        if time in self.times:

            self.ThreadFunction()
            self.times.discard(time)
        
        
    def ThreadFunction(self):
        while True:
            try:
                entity = self.schedule_list[World.time].pop()
                entity.Action()

            except IndexError:
                try:
                    del self.schedule_list[World.time]
                except KeyError:
                    break
            except KeyError:
                break
