# -*- coding: utf-8 -*-

from logic.base.rand import Random
from logic.entities.entity import Entity
from world.world import World
from logic.action import Action
from world.vector2d import Vector2D
from world.action import Walk as WorldWalk



class Walk(Action):
    def __init__(self, world_entity, target_position):
        Action.__init__(self, world_entity)
        self.target_position = target_position
        self.world_action = WorldWalk

    def Start(self, start):
        Action.Start(self, start)
        position = self.world_entity.GetLatest("Position")
        needed = position.CalculateTravelTime(self.target_position)
        self.needed = max(needed, 0.000001)
    def Stop(self, stop):
        if self.IsDone(stop):
            Action.Stop(self, stop)
            self.world_entity.data.Change(stop, "Position", self.target_position)
        else:
            raise Exception("This should never happen: Someone was stopped while he walked")

class Human(Entity):
    def __init__(self, *args, **kwargs):
        Entity.__init__(self, *args, **kwargs)
        self.lifetime = 1000

    def GetNextAction(self, time):
        if time <= self.birth + self.lifetime:
            x = Random.randint(self, 0, World.size_x, seed=time)
            y = Random.randint(self, 0, World.size_y, seed=time + 1)
            target_position = Vector2D(x, y)
            return Walk(self.world_entity, target_position)

