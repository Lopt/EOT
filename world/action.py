# -*- coding: utf-8 -*-

class Action():
    def InTime(self, start, time, stop):
        return start <= time <= stop

    def PercentageDone(self, start, time, stop):
        return (float(time) - start) / (stop - start)

    def Get(self, time, name, data):
        return data.Get(time, name)

    def DoneTime(self):
        pass

class Walk(Action):
    def Get(self, time, name, data):
        if name == "Position":
            start, stop = data.GetInfos(time, name)
            percentage = self.PercentageDone(start, time, stop)
            start_pos = data.Get(start, name)
            stop_pos = data.Get(stop, name)
            return start_pos.CalculatePosition(stop_pos, percentage)
        return Action.Get(self, time, name, data)


