# -*- coding: utf-8 -*-

from entity import Entity

class Town(Entity):
    def __init__(self, name):
        self.name      = name
        self.townfolks = []