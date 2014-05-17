# -*- coding: utf-8 -*-

import copy
from world.world import World
import constants

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
