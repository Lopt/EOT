#coding: utf-8

ID = 0
def CreateID():
    global ID
    ID += 1
    return ID

class Change():
    def __init__(self, obj, function, rfunction, informations):
        self.function     = function
        self.informations = informations
        self.obj          = obj
        self.rfunction    = rfunction
        
    def Apply(self, changes):
        self.function(*self.informations)
    
    def Revert(self, changes):
        self.rfunction(*self.informations)

class Alternative():
    def __init__(self, time, timeline):
        self.time = time
        self.timeline = timeline
        self.changes = []

    def AddChange(self, change):
        self.changes.append(change)

class Time():
    
    def __init__(self):
        self.alternatives = []
    
    def AddAlternative(self, action):
        self.alternatives.append(action)

class Unit():
    def __init__(self, parent, timeline):
        self.childrens = []
        self.parent    = parent
        self.timeline  = timeline

    def CreateUnit(self):
        return Unit(self, self.timeline)
    
    def ActivateUnit(self):
        self.timeline = 1
    
    def DeactivateUnit(self):
        self.timeline = 0


time = Time()
root = Unit(None, CreateID())
a = root.CreateUnit()
aa = root.CreateUnit()
b = root.CreateUnit()
aChange = Change(a, a.ActivateUnit, a.DeactivateUnit, [])
aaChange = Change(aa, aa.ActivateUnit, aa.DeactivateUnit, [])
bChange = Change(b, b.ActivateUnit, b.DeactivateUnit, [])

alternativeT0  = Alternative(0, root.timeline)
alternativeT0.AddChange(aChange)
alternativeT0.AddChange(bChange)
alternativeT0.AddChange(aaChange)

time.AddAlternative(alternative)
