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
        Action.__init__(self, entity, "WALK", World.time, self._CalculateTravelTime(entity.position, target_position))

    def _CalculateTravelTime(self, from_position, to_position):
        return (from_position - to_position).Length() * WALK_FACTOR

    def DoAction(self):
        if self.entity.position != self.target_position:
            self.entity.position = self.entity.CalculatePosition(self.PercentageDone(), self.target_position)

class Chopping(Action):

    def __init__(self, entity, target):
        self.target = target
        Action.__init__(self, entity, "CHOPPING", World.time, CHOPPING_TIME)

    def DoAction(self):
        if self.IsDone():
            if self.target.icon == "T":
                Scheduler.instance.RemoveEntity(self.target)
                self.target.StopAction()
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


    def StopAction(self):
        if self.actions:
            action = self.actions.pop()
            action.DoAction()

            if self.actions:
                self.actions[-1].start = World.time
    
    def GetPosition(self):
        if self.actions:
            action = self.actions[-1]
            if action.action == "WALK":
                return self.CalculatePosition(action.PercentageDone(), action.target_position)
        return self.position

    def CalculatePosition(self, spend_time_factor, target_position):
        return self.position + ((target_position - self.position) * (spend_time_factor / float(WALK_FACTOR)))

    def AddAction(self):
        if not self.actions:
            
            target = self._FindTarget()
            if target is None:
                x = Random.randint(self, 0, World.size_x)
                y = Random.randint(self, 0, World.size_y)
                target_position = Vector2D(x, y)
            else: 
                self.actions.append(Chopping(self, target))
                target_position = target.position                
            
            self.actions.append(Walk(self, target_position))

        self.actions[-1].start_time = World.time
        Scheduler.instance.AddToSchedule(self, self.actions[-1].DoneTime())