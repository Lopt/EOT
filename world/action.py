# -*- coding: utf-8 -*-

class Action(object):
    @staticmethod
    def InTime(start, time, stop):
        return start <= time <= stop

    @staticmethod
    def PercentageDone(start, time, stop):
        return (float(time) - start) / (stop - start)

    @staticmethod
    def Get(time, name, data):
        return data.Get(time, name)

class Walk(Action):
    @staticmethod
    def Get(time, name, data):
        if name == "Position":
            start, stop = data.GetInfos(time, name)
            percentage = Walk.PercentageDone(start, time, stop)
            start_pos = data.Get(start, name)
            stop_pos = data.Get(stop, name)
            return start_pos.CalculatePosition(stop_pos, percentage)
        return Action.Get(time, name, data)

DefaultAction = Action()