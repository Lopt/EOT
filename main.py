# -*- coding: utf-8 -*-

import time

from logic.entities.tree import Tree
from logic.entities.human import Human
from logic.scheduler import Scheduler
from logic.vector2d import Vector2D
from graphic.output import Output
import constants


scheduler = Scheduler()
scheduler.AddEntity(Tree(0,   Vector2D(8, 2)))
scheduler.AddEntity(Tree(53,  Vector2D(7, 2)))

scheduler.AddEntity(Tree(100, Vector2D(0, 4)))
scheduler.AddEntity(Tree(150, Vector2D(0, 5)))
scheduler.AddEntity(Tree(200, Vector2D(0, 6)))
scheduler.AddEntity(Tree(250, Vector2D(1, 5)))

for i in range(constants.NPCS):
    human = Human(i * 100000, Vector2D(0,0), constants.NAMES[i])
    scheduler.AddEntity(human)

scheduler.Schedule(0)

for t in range(constants.ROUNDS):
    #for i in range(1000):

    times = list(scheduler.times)
    
    scheduler.Schedule(t)

        
    Output()
    time.sleep(constants.SLEEP_TIME)


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


