# -*- coding: utf-8 -*-

'''
No NumyPy bescause i want to test it with PyPy
'''

import math

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __sub__(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def ScalarProduct(self, vector):
        return self.x * vector.x + self.y * vector.y
        
    def Length(self):
        return math.sqrt(self.ScalarProduct(self))
        
    def __repr__(self):
        return "(%s, %s)" % (str(self.x), str(self.y))
        
    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y
        
    def CalculatePosition(self, target_position, percentage):
        return self + (target_position - self) * percentage

    def CalculateTravelTime(self, target_position):
        return (self - target_position).Length()