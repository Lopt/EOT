# -*- coding: utf-8 -*-

import copy
from world.world import World
import constants



class Output():
    def __init__(self):
        self.empty_array = [[" " for x in range(World.size_x + 1)] for line in range(World.size_y+ 1)]

    def console(self, time):
        output = copy.deepcopy(self.empty_array)

        for entity in World.entities[time]:
            position = entity.Get(time, "Position")
            icon = entity.Get(time, "Icon")

            output[int(position.x)][int(position.y)] = icon

        for line in output:
            printed_line = ""
            for char in line:
                printed_line += char
            print printed_line

        print '#'*50

'''
import curses


class Output():
    def __init__(self):
        self.empty_array = [" " * World.size_y] * World.size_x
        self.stdscr = curses.initscr()
        curses.curs_set(0)
        self.pad = curses.newpad(World.size_x + 1, World.size_y + 1)

    def curses(self, time):
        for line_nr in range(len(self.empty_array)):
            self.pad.addstr(line_nr, 0, self.empty_array[line_nr])

        for entity in World.entities[time]:
            position = entity.Get(time, "Position")
            icon = entity.Get(time, "Icon")

            self.pad.addch(int(position.x), int(position.y), ord(icon))

        self.pad.refresh(0,0, 0,0, World.size_x+1,World.size_y+1)
'''