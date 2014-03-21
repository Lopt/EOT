# -*- coding: utf-8 -*-

import copy
from logic.world import World
import constants

def Output():
    empty_array = [["." for x in range(World.size_x / 1 + 1)] for line in range(World.size_y / 1 + 1)]
    used_array = copy.deepcopy(empty_array)
    
    for entitie in World.entities:
        position = entitie.GetPosition()
        if (used_array[int(position.x / 1)][int(position.y / 1)] in constants.NAMES):
            pass
        else:
            used_array[int(position.x / 1)][int(position.y / 1)] = entitie.icon
    print 
    for line in used_array:
        printed_line = ""
        for char in line:
            printed_line += char
        print printed_line
    
    #print "" #"-" * 55
