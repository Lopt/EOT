# -*- coding: utf-8 -*-

import constants

class World():
    instance = None

    def __init__(self):
        World.instance = self

    size_x   = constants.WORLD_SIZE_X
    size_y   = constants.WORLD_SIZE_Y
    
    @staticmethod
    def GetEntitiesOnPosition(position):
        return [entity for entity in World.entities if entity.position == position]
    
    @staticmethod
    def IsInWorld(position):
        return (position.x >= 0 and position.x <= World.size_x and
                position.y >= 0 and position.y <= World.size_y)
