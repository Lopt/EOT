# -*- coding: utf-8 -*-

from logic.rand import Random
from logic.entities.type import Type
from logic.world import World
from logic.scheduler import Scheduler
from logic.action import Action
from logic.vector2d import Vector2D

from constants import CHOPPING_TIME, WALK_FACTOR

class Walk(Action):
    def __init__(self, entity, target_position):
        self.target_position = target_position
        Action.__init__(self, entity, "WALK", entity.CalculateTravelTime(entity.position, target_position))


    def Stop(self):
        Action.Stop(self)
        if self.entity.position != self.target_position:
            self.entity.position = self.entity.CalculatePosition(self.PercentageDone(), self.target_position)


class Chopping(Action):
    def __init__(self, entity, target):
        self.target = target
        Action.__init__(self, entity, "CHOPPING", CHOPPING_TIME)

    def Stop(self):
        Action.Stop(self)
        if self.IsDone():
            if self.target.icon == "T":
                self.target.icon = "_"


class Human(Type):
    def __init__(self, entropy, position, name):
        Type.__init__(self, entropy, position, name)
        self.name = name

    def _FindTarget(self):
        entity = Random.choice(self, World.entities)
        if entity.icon == "T":
            return entity
        return None
    
    def GetPosition(self):
        if self.actions:
            action = self.GetAction(World.time)
            if action:
                if action.action == "WALK":
                    return self.CalculatePosition(action.PercentageDone(), action.target_position)
        return self.position

    def CalculatePosition(self, spend_time_factor, target_position):
        return self.position + ((target_position - self.position) * (spend_time_factor / float(WALK_FACTOR)))


    def CalculateTravelTime(self, from_position, to_position):
        return (from_position - to_position).Length() * WALK_FACTOR

    def AddAction(self):
        #target = self._FindTarget()
        if True: #target is None:
            while True:
                x = Random.randint(self, 0, World.size_x)
                y = Random.randint(self, 0, World.size_y)
                target_position = Vector2D(x, y)

                if  self.CalculateTravelTime(self.position, target_position) > 1:
                    break
        #else:
        #    self.actions[World.time] = Chopping(self, target)
        #    target_position = target.position

        self.actions[World.time] = Walk(self, target_position)
        self.actions[World.time].Activate()


