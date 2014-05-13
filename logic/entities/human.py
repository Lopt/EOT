# -*- coding: utf-8 -*-
from logic.automat.scheduler import Scheduler

from logic.base.rand import Random
from logic.entities.entity import Entity
from logic.world import World
from logic.automat.action import Action
from logic.base.vector2d import Vector2D

from constants import CHOPPING_TIME, WALK_FACTOR

class Walk(Action):
    def __init__(self, entity, target_position):
        current_time = Scheduler.instance.time
        self.target_position = target_position
        Action.__init__(self, entity, "WALK")

    def Start(self, start):
        self.needed = self.entity.CalculateTravelTime(self.entity.data.Get(start, "Position"), self.target_position)
        self.needed = max(self.needed, 0.001)
        Action.Start(self, start)

    def Stop(self, stop):
        position = self.entity.data.Get(stop, "Position")
        Action.Stop(self, stop)
        if position != self.target_position:
            position = self.entity.CalculatePosition(self.PercentageDone(stop), position, self.target_position)
            self.entity.data.Change(stop, "Position", position)

class Human(Entity):
    def __init__(self, time, position, name):
        Entity.__init__(self, time, position, name)
    
    def GetPosition(self):
        if self.actions:
            action = self.GetAction(World.time)
            if action:
                if action.action == "WALK":
                    return self.CalculatePosition(action.PercentageDone(), action.target_position)
        return self.position

    def CalculatePosition(self, spend_time_factor, from_position, target_position):
        return from_position + ((target_position - from_position) * (spend_time_factor / float(WALK_FACTOR)))

    def CalculateTravelTime(self, from_position, to_position):
        return (from_position - to_position).Length() * WALK_FACTOR

    def CalculateAction(self, time):
        x = Random.randint(self, 0, World.size_x, 1)
        y = Random.randint(self, 0, World.size_y, 2)
        target_position = Vector2D(x, y)
        self.next_actions.append(Walk(self, target_position))



