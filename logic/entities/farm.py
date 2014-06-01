# -*- coding: utf-8 -*-

from logic.entities.entity import Entity
from logic.action import Action
from logic.lifetime import Calculate
from world.action import DefaultAction
from world.world import World
from logic.base.rand import Random
from world.vector2d import Vector2D
from logic.scheduler import Scheduler


class Grow(Action):
    def OnInit(self):
        self.needed = Calculate(days=7)

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.world_entity.data.Change(time, "Icon", u"=")

class Farm(Entity):
    def OnInit(self, time):
        self.world_entity.data.Change(time, "Icon", u"-")

    def GetNextAction(self, time):
        if self.world_entity.GetLatest("Icon") == u"-":
            return Grow(self)

        else:
            return Action(self)
