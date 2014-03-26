# -*- coding: utf-8 -*-

from logic.world import World

class Action():

    def __init__(self, entity, action, start_time, needed_time):
        self.entity      = entity
        self.start_time  = start_time
        self.needed_time = needed_time
        self.action      = action
    
    def IsDone(self):
        return self.start_time + self.needed_time >= World.time
    
    def DoneTime(self):
        return self.start_time + self.needed_time

    def PercentageDone(self):
        return (float(World.time) - self.start_time) / self.needed_time

    def DoAction(self):
        pass

    def __repr__(self):
        return "<Type: %s Time: %i Target %s>" % (self.action, self.start_time, self.target)
        
