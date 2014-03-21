# -*- coding: utf-8 -*-

from logic.entities.type import Type
from logic.action import Action
from logic.world import World
from logic.rand import Random
from logic.vector2d import Vector2D
from logic.scheduler import Scheduler
import constants

class Tree(Type):
    def __init__(self, entropie, position):
        Type.__init__(self, entropie, position, "t")
    
        self.plant_time = 0
                
        
    def StopAction(self):
        action = self.actions.pop()
        if action.action == "GROW":
            if action.IsDone():
                self.icon = "T"
        if action.action == "PLANT":
            if action.IsDone():
                addx = Random.randint(self, -1, 1)
                addy = Random.randint(self, -1, 1)
                plant_position = self.position + Vector2D(addx, addy)
                if World.IsInWorld(plant_position):
                    if not World.GetEntitiesOnPosition(plant_position):
                        entropie = Random.randint(self, 0, 100000)                                    
                        Scheduler.instance.AddEntity(Tree(entropie, plant_position))

    def AddAction(self):
        if not self.actions:
            grow_time = constants.GROW_TIME
            self.plant_time += constants.RESEED_TIME
            
            if self.icon == "_":
                return None
            if self.icon == "t":
                self.actions.append(Action(World.time, grow_time + Random.randint(self, 0, 10), "GROW", None))
            elif self.icon == "T":
                self.actions.append(Action(World.time, self.plant_time + Random.randint(self, 0, 10), "PLANT", None))        
    
            Scheduler.instance.AddToSchedule(self, self.actions[-1].DoneTime())
    
    
    def Chopped(self):
        Scheduler.instance.RemoveEntity(self)
        self.StopAction()
        self.icon = "_"