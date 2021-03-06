# -*- coding: utf-8 -*-
import copy

import constants
from timedict import TimeDict


class World(object):
    entities = TimeDict({-1: []})

    size_x   = constants.WORLD_SIZE_X
    size_y   = constants.WORLD_SIZE_Y

    @staticmethod
    def IsInWorld(position):
        return (0 <= position.x <= World.size_x and
                0 <= position.y <= World.size_y)

    @staticmethod
    def GetEntititiesInRange(time, start, end):
        entities = []
        for entity in World.entities[time]:
            entity_pos = entity.data.Get(time, "Position")
            if (start.x < entity_pos.x < end.x and
                start.y < entity_pos.y < end.y):
                entities.append(entity)
        return entities


    @staticmethod
    def GetEntitiesOnPosition(time, position):
        entities = []
        for entity in World.entities[time]:
            if entity.data.Get(time, "Position") == position:
                entities.append(entity)
        return entities

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

