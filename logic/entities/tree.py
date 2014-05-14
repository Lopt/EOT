# -*- coding: utf-8 -*-

from logic.entities.entity import Entity
from logic.action import Action
from world.world import World
from logic.base.rand import Random
from world.vector2d import Vector2D

from constants import RESEED_TIME, GROW_TIME

class Grow(Action):

    def Start(self, time):
        Action.Start(self, time)
        self.stop = time + 10

    def Stop(self, time):
        Action.Stop(self, time)
        if time >= self.stop:
            self.world_entity.data.Change(time, "Icon", "T")

class Plant(Action):
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

class Tree(Entity):

    def GetNextAction(self, time):
        if self.world_entity.GetLatest("Icon") == "t":
            return Grow(self.world_entity)
        if self.world_entity.GetLatest("Icon") == "T":
            return Grow(self.world_entity)
