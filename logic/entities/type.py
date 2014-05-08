# -*- coding: utf-8 -*-
import sys
import bisect

class Type():
    def __init__(self, entropy, position, icon = ""):
        self.icon     = icon
        self.position = position
        self.entropy  = entropy
        self.actions  = {}
        self.next_actions = []
    
    def GetPosition(self):
        return self.position

    def Action(self, time):
        last_action = self.GetAction(time)
        if last_action:
            last_action.Stop()

        current_action = self.GetAction(time + 1)
        if current_action is None:
            self.AddAction()
            current_action = self.GetAction(time + 1)

        current_action.Start()

    def GetAction(self, time):
        keys = sorted(self.actions.keys())
        index = bisect.bisect(keys, time)
        action = self.actions[keys[index - 1]]
        if action.InRange(time):
            return action
        return None

    def AddAction(self):
        pass

    def __repr__(self):
        return self.icon
        
