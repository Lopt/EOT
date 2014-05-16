# -*- coding: utf-8 -*-

from logic.base.rand import Random
from logic.entities.entity import Entity
from world.world import World
from logic.action import Action
from world.vector2d import Vector2D
from world.action import Walk as WorldWalk



class Walk(Action):
    def OnInit(self, target_position):
        self.target_position = target_position
        self.world_action = WorldWalk()

    def OnStart(self, time):
        position = self.world_entity.GetLatest("Position")
        needed = position.CalculateTravelTime(self.target_position)
        self.needed = max(needed, 0.000001)

    def OnStop(self, time):
        if self.IsDone(time):
            self.world_entity.data.Change(time, "Position", self.target_position)
        else:
            raise Exception("This should never happen: Someone was stopped while he walked")

class Human(Entity):
    def OnInit(self, time, name):
        self.world_entity.data.Change(time, "Icon", name)
        self.lifetime = 1000

    def GetNextAction(self, time):
        if time <= self.birth + self.lifetime:
            x = Random.randint(self, 0, World.size_x, seed=time)
            y = Random.randint(self, 0, World.size_y, seed=time + 1)
            target_position = Vector2D(x, y)
            return Walk(self.world_entity, target_position)

