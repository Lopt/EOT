# -*- coding: utf-8 -*-

import copy

from world.world import World
import constants


def Output(time):
    empty_array = [["." for x in range(World.size_x / 1 + 1)] for line in range(World.size_y / 1 + 1)]
    used_array = copy.deepcopy(empty_array)

    for entity in World.entities:
        position = entity.Get(time, "Position")
        if (used_array[int(position.x)][int(position.y)] in constants.NAMES):
            pass
        else:
            used_array[int(position.x)][int(position.y)] = entity.Get(time, "Icon")
    print 
    for line in used_array:
        printed_line = ""
        for char in line:
            printed_line += char
        print printed_line
    
    #print "" #"-" * 55
