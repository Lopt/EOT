# -*- coding: utf-8 -*-
import constants

from logic.entities.entity import Entity
from logic.action import Action
from logic.lifetime import Calculate
from world.world import World
from logic.base.rand import Random
from world.vector2d import Vector2D
from logic.scheduler import Scheduler

class Grow(Action):
    def OnInit(self):
        self.needed = constants.FARM_GROW_TIME

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.Change(time, "Icon", "T")

class OnChoped(Action):
    def OnInit(self):
        self.needed = constants.HUMAN_CHOPPING_TIME

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.Change(time, "Icon", "_")

class Plant(Action):
    def OnInit(self):
        self.needed = Calculate(years=1)

    def OnStop(self, time):
        if self.IsDone(time):
            add_x = Random.randint(self.world_entity, -1, 1, seed=time)
            add_y = Random.randint(self.world_entity, -1, 1, seed=time + 1)
            plant_position = self.entity.Get(time, "Position") + Vector2D(add_x, add_y)

            if World.IsInWorld(plant_position):
                if not World.GetEntitiesOnPosition(time, plant_position):
                    entropy = Random.random(self.world_entity, seed=time)
                    Scheduler.instance.CreateEntity(Tree, entropy, plant_position)

class Tree(Entity):
    def OnInit(self, time):
        self.Change(time, "Icon", "t")
        self.replants = 10

    def CreateNextAction(self, time):
        if self.replants:
            if self.GetLatest("Icon") == "t":
                return Grow(self.world_entity)
            if self.GetLatest("Icon") == "T":
                self.replants -= 1
                return Plant(self)
        else:
            return Action(self)
