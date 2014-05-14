# -*- coding: utf-8 -*-
from collections import deque
from world.entity import Entity as WorldEntity


class Entity():
    def __init__(self, time, position, icon):
        self.current_action = None
        self.world_entity = WorldEntity(time, {"Position": position, "Icon": icon})

    def GetAction(self, time):
        return self.current_action

    def GetNextAction(self, time):
        return None

    def SetAction(self, time, action):
        self.current_action = action