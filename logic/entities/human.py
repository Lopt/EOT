# -*- coding: utf-8 -*-
import constants

from logic.base.rand import Random
from logic.entities.entity import Entity
from world.world import World
from logic.action import Action
from logic.entities.farm import OnFarmed
from world.vector2d import Vector2D
from world.action import Walk as WorldWalk


class Walk(Action):
    def OnInit(self, target_position):
        self.target_position = target_position
        self.world_action = WorldWalk

    def OnStart(self, time):
        position = self.entity.GetLatest("Position")
        needed = position.CalculateTravelTime(self.target_position) * constants.HUMAN_WALK_FACTOR
        self.needed = max(needed, 1)

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.Change(time, "Position", self.target_position)
        else:
            raise Exception("This should never happen: Someone was stopped while he walked")

class Farm(Action):
    def OnInit(self, target):
        self.needed = constants.HUMAN_FARMING_TIME
        self.target = target

    def BeforeStart(self):
        target_pos = self.entity.GetLatest("Position")
        entity_pos = self.entity.GetLatest("Position")

        if not (target_pos == entity_pos):
            return [Walk(self.entity, Vector2D(target_pos.x, target_pos.y))]
        return []

    def OnStop(self, time):
        if self.IsDone(time):
            self.target.SetAction(time, OnFarmed(self.target))

class Human(Entity):
    def OnInit(self, time, name):
        self.target = None

        self.Change(time, "Icon", name)
        self.lifetime = constants.HUMAN_LIFETIME

    def _FindFarm(self, time):
        for entity in World.entities[time]:
            if entity.GetLatest("Icon") == '=':
                return entity.GetLogicEntity()

    def _RandomWalk(self, time):
        x = Random.randint(self, 0, World.size_x, seed=time)
        y = Random.randint(self, 0, World.size_y, seed=time + 1)
        target_position = Vector2D(x, y)
        return Walk(self, target_position)

    def CreateNextAction(self, time):
        if time > self.birth + self.lifetime:
            return

        if not self.next_actions:
            target = self._FindFarm(time)
            if target is None:
                action = self._RandomWalk(time)
            else:
                action = Farm(self, target)

            return action


