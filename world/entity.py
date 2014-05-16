# -*- coding: utf-8 -*-

from timedata import Data
from timedict import TimeDict
from vector2d import Vector2D

from action import Walk
from world import World


class Entity():
    def __init__(self, time, entropy, *args, **kwargs):
        self.entropy = entropy
        self.data = Data(time, *args, **kwargs)
        self.actions = TimeDict()

        World.AppendEntity(time, self)

    def Kill(self, time):
        self.data.Kill(time)
        World.RemoveEntity(time, self)

    def GetLatest(self, name):
        return self.data.GetLatest(name)

    def Get(self, time, name):
        return self.actions[time].Get(time, name, self.data)

    def AddAction(self, time, action):
        self.actions[time] = action

if __name__ == "__main__":

    e = Entity(0, {"Position": Vector2D(0, 0)})
    e.data.Change(10, "Position", Vector2D(1, 1))
    e.data.Change(20, "Position", Vector2D(2, 2))
    e.data.Change(50, "Position", Vector2D(3, 3))
    e.data.Change(100, "Position", Vector2D(4, 4))

    e.AddAction(0, Walk())
    e.AddAction(10, Walk())
    e.AddAction(50, Walk())

    print e.Get(0, "Position")
    print e.Get(1, "Position")
    print e.Get(10, "Position")
    print e.Get(49, "Position")
    print e.Get(50, "Position")
    print e.Get(99, "Position")
    print e.Get(100, "Position")
