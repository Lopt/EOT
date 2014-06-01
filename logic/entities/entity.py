# -*- coding: utf-8 -*-
from collections import deque
from world.entity import Entity as WorldEntity


class Entity():
    def __init__(self, time, entropy, position, *args, **kwargs):
        self.birth = time
        self.entropy = entropy
        self.current_action = None
        self.next_actions = []
        self.world_entity = WorldEntity(self, time, entropy, {"Position": position})
        self.OnInit(time, *args, **kwargs)

    def GetAction(self, time):
        return self.current_action

    def GetNextAction(self, time):
        return None

    def SetAction(self, time, action):
        if self.current_action:
            self.current_action.Stop(time)

        self.current_action = action
        if action:
            action.Start(time)