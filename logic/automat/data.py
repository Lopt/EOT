# -*- coding: utf-8 -*-

import bisect
from time_exception import TimeException

class Data():
    def __init__(self, time, standard):
        self.times = {}
        self.data  = {}

        for name in standard:
            self.times[name] = []
            self.data[name]  = {}
            self.Change(time, name, standard[name])

    def Change(self, time, name, value):
        times = self.times[name]
        index = bisect.bisect(times, time)
        if time not in times:
            times.insert(index, time)
        self.data[name][time] = value

    def Get(self, time, name):
        times = self.times[name]
        index = bisect.bisect(times, time)
        if index:
            start_time = times[index - 1]
            try:
                return self.data[name][start_time]
            except KeyError:
                pass
        else:
            raise TimeException("Value doesn't exist yet")


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
