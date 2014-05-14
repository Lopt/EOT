# -*- coding: utf-8 -*-
import copy

import constants
from timedict import TimeDict


class World():
    entities = TimeDict({-1: []})

    size_x   = constants.WORLD_SIZE_X
    size_y   = constants.WORLD_SIZE_Y

    @staticmethod
    def IsInWorld(position):
        return (position.x >= 0 and position.x <= World.size_x and
                position.y >= 0 and position.y <= World.size_y)

    @staticmethod
    def AppendEntity(time, entity):
        entities = copy.copy(World.entities[time])
        entities.append(entity)
        World.entities[time] = entities

    @staticmethod
    def RemoveEntity(time, entity):
        entities = copy.copy(World.entities[time])
        entities.remove(entity)
        World.entities[time] = entities


