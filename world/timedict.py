# -*- coding: utf-8 -*-

from bisect import bisect
from copy import copy

class TimeDict():

    def __init__(self, standard = dict()):
        self.times = standard.keys()
        self.data = copy(standard)

    def __getitem__(self, time):
        index = bisect(self.times, time)
        if index:
            return self.data[self.times[index - 1]]
        raise KeyError()

    def __len__(self):
        return len(self.times)

    def GetLatest(self):
        return self.data[self.times[-1]]

    def __setitem__(self, time, data):
        index = bisect(self.times, time)
        if not index or self.times[index - 1] != time:
            self.times.insert(index, time)
        self.data[time] = data
