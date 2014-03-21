# -*- coding: utf-8 -*-

from type import Type

class Town(Type):
    def __init__(self, name):
        self.name      = name
        self.townfolks = []