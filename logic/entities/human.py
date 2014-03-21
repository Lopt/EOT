# -*- coding: utf-8 -*-

from logic.rand import Random
from logic.entities.type import Type
from logic.world import World
from logic.scheduler import Scheduler

from logic.action import Action
from logic.vector2d import Vector2D
import constants

class Human(Type):
    def __init__(self, entropie, position, name):
        Type.__init__(self, entropie, position, name)
        self.name = name
        
        
    def _FindTarget(self):
        entity = Random.choice(self, World.entities)
        if entity.icon == "T":
            return entity
        return None

    def _CalculateTravelTime(self, from_position, to_position):
        return (from_position - to_position).Length() * constants.WALK_FACTOR
    
    def StopAction(self):
        action = self.actions.pop()
        if action.action == "WALK":
            self.position = self.CalculatePosition(action.PercentageDone(), action.target)
        
        elif action.action == "CHOPPING":
            if action.IsDone():
                if action.target.icon == "T":
                    action.target.Chopped()
            
        if self.actions:
            self.actions[-1].start = World.time
    
    def GetPosition(self):
        if self.actions:
            action = self.actions[-1]
            if action.action == "WALK":
                return self.CalculatePosition(action.PercentageDone(), action.target)
        return self.position
        
    
    def CalculatePosition(self, spend_time_factor, target_position):
        return self.position + ((target_position - self.position) * (spend_time_factor / float(constants.WALK_FACTOR)))
        
            
    def AddAction(self):
        if not self.actions:
            chopping_time = 10       
            
            target = self._FindTarget()
            if target is None:
                x = Random.randint(self, 0, World.size_x)
                y = Random.randint(self, 0, World.size_y)
                target_position = Vector2D(x, y)
            else: 
                self.actions.append(Action(World.time, chopping_time, "CHOPPING", target))
                target_position = target.position                
            
            if target_position == self.position:                
                time = 1
            else:
                time = self._CalculateTravelTime(self.position, target_position)
            self.actions.append(Action(World.time, time, "WALK", target_position))

        self.actions[-1].start_time = World.time
        Scheduler.instance.AddToSchedule(self, self.actions[-1].DoneTime())