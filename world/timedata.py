# -*- coding: utf-8 -*-

import bisect
from time_exception import TimeException
import sys

class Data(object):
    def __init__(self, time, standard):
        self.times = {}
        self.data = {}
        self.death = sys.maxint

        for name in standard:
            self.times[name] = []
            self.data[name]  = {}
            self.Change(time, name, standard[name])

    def Change(self, time, name, value):
        if not self.times.has_key(name):
            self.times[name] = [time]
            self.data[name] = {time: value}

        times = self.times[name]
        index = bisect.bisect(times, time)
        if time not in times:
            times.insert(index, time)
        self.data[name][time] = value

    def Kill(self, time):
        self.death = time

    def Get(self, time, name):
        if time <= self.death:
            times = self.times[name]
            index = bisect.bisect(times, time)
            if index:
                start_time = times[index - 1]
                try:
                    return self.data[name][start_time]
                except KeyError:
                    pass
            else:
                raise TimeException("Data doesn't exist yet")
        else:
            raise TimeException("Data doesn't exist anymore")

    def GetLatest(self, name):
        return self.data[name][self.times[name][-1]]

    def GetInfos(self, time, name):
        if time <= self.death:
            times = self.times[name]
            index = bisect.bisect(times, time)
            if index > 0:
                start = times[index - 1]
                stop = times[index]
                return [start, stop]
