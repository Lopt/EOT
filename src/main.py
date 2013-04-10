#coding: utf-8

class Timeline():
    
    def __init__(self, parent):
        self.parent = parent
        self.active = 0
        self.timelines = [[], []]
    
    def PrintTimeline(self):
        for changes in self.timelines:
            for children in changes:
                if children:
                    children.PrintTimeline()
    
    def ChangeTimeline(self):
        self.active = not self.active
    
class Unit(Timeline):
    
    def CreateUnit(self):
        unit = Unit(self)
        self.timelines[self.active].append(unit)
        return unit

    def PrintTimeline(self):
        Timeline.PrintTimeline(self)
        print "Test"


    

company = Unit(None)
unit1 = company.CreateUnit()
unit2 = company.CreateUnit()

