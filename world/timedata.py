# -*- coding: utf-8 -*-

import bisect
from time_exception import TimeException
import sys

class Data():
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

if __name__ == "__main__":


    from datetime import datetime, timedelta

    td = timedelta()

    datas = []
    for i in xrange(100):
        start = datetime.now()

        datadict = {}
        for k in xrange(16):
            datadict["D" + str(k)] = 0

        d = Data(0, datadict)
        datas.append(d)
        for j in xrange(1, 100):
            for k in xrange(16):
                nr = "D" + str(k)
                d.Change(j * 1000, nr, j)

                d.Get(j * 1000, nr)
                d.Get(j * 1000 - 1, nr)
                d.Get(j, nr)
                d.Get(j, nr)
                d.Get(j, nr)
        print i
        end = datetime.now()
        td += end - start

    print td
    raw_input()
    datas.clear()
