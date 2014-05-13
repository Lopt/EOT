# -*- coding: utf-8 -*-
from collections import deque
import sys
from bisect import bisect
from logic.automat.data import Data


class Entity():
    def __init__(self, time, position, icon):
        self.actions = {}
        self.next_actions = deque()
        self.data = Data(time, {"Position": position, "Icon": icon})

    def GetPosition(self):
        return self.position

    def GetAction(self, time):
        times = sorted(self.actions.keys())
        index = bisect(times, time)
        if index:
            last_time = times[index - 1]
            action = self.actions[last_time]
            if action.InTime(time):
                return action
        return None

    def ExecuteAction(self, time):
        last_action = self.GetAction(time)
        if last_action:
            last_action.Stop(time)

        next_action = self.GetAction(time + 1)
        if not next_action:
            self.CalculateAction(time)

            next_action = self.next_actions.popleft()
            self.actions[time] = next_action

        next_action.Start(time)

    def CalculateAction(self):
        pass