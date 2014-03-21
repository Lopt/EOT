# -*- coding: utf-8 -*-

from logic.world import World

class Action():

    def __init__(self, start_time, needed_time, action, target):
        self.start_time  = start_time
        self.needed_time = needed_time
        self.action      = action
        self.target      = target
    
    def IsDone(self):
        return self.start_time + self.needed_time >= World.time
    
    def DoneTime(self):
        return self.start_time + self.needed_time

    def PercentageDone(self):
        return (float(World.time) - self.start_time) / self.needed_time
    
    def __repr__(self):
        return "<Type: %s Time: %i Target %s>" % (self.action, self.start_time, self.target)
        
