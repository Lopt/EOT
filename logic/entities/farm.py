# -*- coding: utf-8 -*-
import constants

from logic.entities.entity import Entity
from logic.action import Action


class Grow(Action):
    def OnInit(self):
        self.needed = constants.FARM_GROW_TIME

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.Change(time, "Icon", u"=")

class OnFarmed(Action):
    def OnInit(self):
        self.needed = constants.HUMAN_FARMING_TIME

    def OnStop(self, time):
        if self.IsDone(time):
            self.entity.Change(time, "Icon", "-")

class Farm(Entity):
    def OnInit(self, time):
        self.Change(time, "Icon", u"-")

    def CreateNextAction(self, time):
        if self.GetLatest("Icon") == u"-":
            return Grow(self)
        else:
            return Action(self)
