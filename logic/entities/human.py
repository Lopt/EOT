# -*- coding: utf-8 -*-

from logic.base.rand import Random
from logic.entities.entity import Entity
from world.world import World
from logic.action import Action, Death
from world.vector2d import Vector2D
from world.action import Walk as WorldWalk


class Walk(Action):
    def __init__(self, world_entity, target_position):
        self.target_position = target_position

        self.world_entity = world_entity
        self.world_action = WorldWalk()
        Action.__init__(self, world_entity)

    def Start(self, start):
        Action.Start(self, start)
        position = self.world_entity.GetLatest("Position")
        needed = position.CalculateTravelTime(self.target_position)
        needed = max(needed, 0.00001)
        self.stop = self.start + needed

    def Stop(self, stop):
        Action.Stop(self, stop)
        self.world_entity.data.Change(stop, "Position", self.target_position)

class Human(Entity):
    def __init__(self, *args, **kwargs):
        Entity.__init__(self, *args, **kwargs)

    def GetNextAction(self, time):
        x = Random.randint(self, 0, World.size_x, 1)
        y = Random.randint(self, 0, World.size_y, 2)
        target_position = Vector2D(x, y)
        return Walk(self.world_entity, target_position)

