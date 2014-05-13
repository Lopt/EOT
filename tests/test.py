














ID = 0
def CreateID():
    global ID
    ID += 1
    return ID

def EmptyFunction():
    return None

class Action():
    
    '''
    time: the time this happended
    function: function which will be called when the action is taken
    rfunction: function which will be called when the action should be reversed
    information: additional informations for the pfunctions/rfunction/function
    '''    
    def __init__(self, time):
        self.id      = CreateID()
        self.time    = time
        self.actions = {}
        self.active  = False
        
    def GetTime(self):
        return self.time
            
    def Apply(self, max_time = 0):
        if not self.active:
            self.OnApply(max_time)
            self.active = True
        
        times = self.actions.keys()
        times.sort()

        for time in times:
            if time <= max_time:
                for action in self.actions[time]:
                    action.Apply(max_time)
                
    
    def Revert(self, min_time = 0):
        times = self.actions.keys()
        times.sort()
        times.reverse()
        
        for time in times:
            if time >= min_time:
                for action in self.actions[time]:
                    action.Revert(min_time)      
                    
        if self.active:
            self.OnRevert(min_time)
            self.active = False
    
    def OnApply(self, max_time = 0):
        pass
    
    def OnRevert(self, min_time = 0):
        pass

    def AddAction(self, action):
        if not self.actions.has_key(action.time):
            self.actions[action.time] = []

        self.actions[action.time].append(action)

class UnitManager():
    units = []        
    
    @staticmethod
    def Print():
        for unit in UnitManager.units:
            print unit.GetName()

    @staticmethod
    def AddUnit(unit):
        UnitManager.units.append(unit)

    @staticmethod
    def RemoveUnit(unit):
        UnitManager.units.remove(unit)


class Death(Action):
    def __init__(self, time, killer, killed_unit):
        Action.__init__(self, time)
        self.killer      = killer
        self.killed_unit = killed_unit
        
    def OnApply(self, max_time = 0):
        self.killed_unit.Revert(max_time)
        
    def OnRevert(self, min_time = 0):
        self.killed_unit.Apply(min_time)
        

class Unit(Action):
    def __init__(self, time, name):
        Action.__init__(self, time)
        self.name = name

    def GetName(self):
        return self.name        
    
    def OnApply(self, max_time = 0):
        UnitManager.AddUnit(self)
        
    def OnRevert(self, min_time = 0):
        UnitManager.RemoveUnit(self)

    def Kill(self, time, unit):
        self.AddAction(Death(time, self, unit))

time = 0
root = Action(time)

time = 10;
test1 = Unit(time, "Leto")
root.AddAction(test1)

kill1 = Unit(time + 1, "Killer")
root.AddAction(kill1)

time = 20;
test2 = Unit(time, "Leto2")
test1.AddAction(test2)

time = 30;
test3 = Unit(time, "Leto3")
test2.AddAction(test3)

kill1.Kill(35, test2)

UnitManager.Print()
print '##'*20
root.Apply(36)
UnitManager.Print()
