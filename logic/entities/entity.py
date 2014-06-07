# -*- coding: utf-8 -*-

from world.entity import Entity as WorldEntity


class Entity():
    def __init__(self, time, entropy, position, *args, **kwargs):
        self.birth = time
        self.entropy = entropy
        self.current_action = None
        self.next_actions = []
        self.world_entity = WorldEntity(self, time, entropy, {"Position": position})
        self.OnInit(time, *args, **kwargs)

    def Change(self, *args, **kwargs):
        return self.world_entity.data.Change(*args, **kwargs)

    def Get(self, *args, **kwargs):
        return self.world_entity.Get(*args, **kwargs)

    def GetLatest(self, *args, **kwargs):
        return self.world_entity.GetLatest(*args, **kwargs)

    def GetAction(self, time):
        return self.current_action

    def GetNextAction(self, time):
        if not self.next_actions:
            action = self.CreateNextAction(time)
            if not action: return
            self.next_actions.append(action)

        self._ActionBeforeStart(self.next_actions[0])
        return self.next_actions.pop(0)

    def _ActionBeforeStart(self, action):
        before_actions = action.BeforeStart()
        if before_actions:
            self.next_actions = before_actions + self.next_actions
            self._ActionBeforeStart(self.next_actions[0])

    def CreateNextAction(self):
        pass

    def SetAction(self, time, action):
        if self.current_action:
            self.current_action.Stop(time)

        self.current_action = action
        if action:
            action.Start(time)