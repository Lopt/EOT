# -*- coding: utf-8 -*-

import datetime

from logic.entities.human import Human
from logic.entities.tree import Tree
from logic.scheduler import Scheduler
from world.vector2d import Vector2D
from world.world import World
from graphic.output import Output
from time import sleep
import constants

start = datetime.datetime.now()

scheduler = Scheduler()


for i in range(constants.NPCS):
    scheduler.CreateEntity(Human, i, Vector2D(0,0), constants.NAMES[i])

scheduler.CreateEntity(Tree, 1, Vector2D(5,5))
scheduler.CreateEntity(Tree, 2, Vector2D(5,6))
scheduler.CreateEntity(Tree, 3, Vector2D(6,5))
scheduler.CreateEntity(Tree, 4, Vector2D(6,6))

scheduler.Schedule(0, constants.ROUNDS)


end = datetime.datetime.now()


for time in range(constants.ROUNDS):

    #print World.entities[time][0].Get(time, "Position")
    Output(time)
    sleep(constants.SLEEP_TIME)

end2 = datetime.datetime.now()

print "Dauer Datenerzeugung:", end - start
print "Dauer Datenlesen:", end2 - end

raw_input("TEST")

World.entities

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


