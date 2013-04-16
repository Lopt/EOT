#coding: utf-8

class TimeList(list):
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        self.sort(cmp=TimeList.compare)

    @staticmethod
    def compare(obj1, obj2):
        return obj1.GetTime() < obj2.GetTime()
        
    def append(self, *args, **kwargs):
        list.append(self, *args, **kwargs)
        self.sort(cmp=TimeList.compare)

    def insert(self, *args, **kwargs):
        list.insert(self, *args, **kwargs)
        self.sort(cmp=TimeList.compare)
        
ID = 0
def CreateID():
    global ID
    ID += 1
    return ID

class Alternative():
    def __init__(self):
        self.changes = TimeList()
        
    def AddChange(self, change):
        self.changes.append(change)

class Change():
    def __init__(self, time, function, rfunction, informations):
        self.function     = function
        self.informations = informations
        self.time         = time
        self.rfunction    = rfunction
        
    def GetTime(self):
        return self.time
    
    def Apply(self, changes):
        self.function(*self.informations)
    
    def Revert(self, changes):
        self.rfunction(*self.informations)


class Timeline():
    def __init__(self):
        self.alternatives = {}
        
    def AddChange(self, time, change):
        alternative = Alternative()
        if not self.alternatives.has_key(time):
            self.alternatives[time] = []

        alternative.AddChange(change)
        self.alternatives[time].append(alternative)

class Unit(Timeline):
    def __init__(self, parent):
        Timeline.__init__(self)
        self.parent    = parent

    def CreateUnit(self, time):
        unit = Unit(self)
        change = Change(time,  unit.ActivateUnit, unit.DeactivateUnit, [])
        self.AddChange(time, change)
        return unit

    def ActivateUnit(self):
        pass
    
    def DeactivateUnit(self):
        pass


root = Unit(None)
a = root.CreateUnit(0)
b = root.CreateUnit(0)

aa = a.CreateUnit(1)
bb = b.CreateUnit(1)


