# -*- coding: utf-8 -*-

import constants

class World():
    entities = []

    size_x   = constants.WORLD_SIZE_X
    size_y   = constants.WORLD_SIZE_Y

    @staticmethod
    def IsInWorld(position):
        return (position.x >= 0 and position.x <= World.size_x and
                position.y >= 0 and position.y <= World.size_y)
