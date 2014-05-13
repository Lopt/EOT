# -*- coding: utf-8 -*-

from logic.entities.human import Human
from logic.automat.scheduler import Scheduler
from logic.base.vector2d import Vector2D
from logic.world import World

import constants

import datetime

start = datetime.datetime.now()

scheduler = Scheduler()
world     = World()


for i in range(constants.NPCS):
    human = Human(0, Vector2D(0,0), constants.NAMES[i])
    human.ExecuteAction(0)

for t in range(constants.ROUNDS):
    times = list(scheduler.times)
    
    scheduler.Schedule(t)
        
    #Output()
    #time.sleep(constants.SLEEP_TIME)

end = datetime.datetime.now()

print "Dauer:", end - start

raw_input("TEST")
print len(human.actions)

'''
while True:
    times = list(scheduler.times)
    times.sort()
    if times: 
        scheduler.Schedule(times[0])

        time.sleep(0.1)
        Output()
            
    else:
        break

#print A.actions
#print B.actions
#print C.actions
#print D.actions



'''


