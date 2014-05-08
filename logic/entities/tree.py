# -*- coding: utf-8 -*-

from logic.entities.type import Type
from logic.action import Action
from logic.world import World
from logic.rand import Random
from logic.vector2d import Vector2D
from logic.scheduler import Scheduler

from constants import RESEED_TIME, GROW_TIME

class Grow(Action):
    def __init__(self, entity):
        Action.__init__(self, entity, "GROW", GROW_TIME)

    def Stop(self):
        Action.Stop(self)
        if self.IsDone():
            self.entity.icon = "T"

class Plant(Action):
    def __init__(self, entity):
        Action.__init__(self, entity, "PLANT", RESEED_TIME)

    def Stop(self):
        Action.Stop(self)
        if self.IsDone():
            addx = Random.randint(self.entity, -1, 1)
            addy = Random.randint(self.entity, -1, 1)
            plant_position = self.entity.position + Vector2D(addx, addy)

            if World.IsInWorld(plant_position):
                if not World.GetEntitiesOnPosition(plant_position):
                    entropy = Random.randint(self.entity, 0, 100000)

                    #tree = Tree(entropy, plant_position)
                    #World.entities.append(tree)

class Tree(Type):
    def __init__(self, entropy, position):
        Type.__init__(self, entropy, position, "t")
        self.plant_time = 0

    def AddAction(self):
        if self.icon == "_":
            return None
        if self.icon == "t":
            self.actions[World.time] = Grow(self)
        elif self.icon == "T":
            self.actions[World.time] = Plant(self)