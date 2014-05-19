# -*- coding: utf-8 -*-

import datetime
import json
import pickle
import cPickle
from logic.action import Action

from logic.entities.human import Human
from logic.entities.farm import Farm
from logic.lifetime import Calculate
from logic.scheduler import Scheduler
from world.decoder import ObjectEncoder
from world.vector2d import Vector2D
from world.world import World
from graphic.output import Output
from time import sleep
import constants

scheduler = Scheduler()

for i in xrange(constants.NPCS):
    scheduler.CreateEntity(Human, i, Vector2D(0,0), constants.NAMES[i])

scheduler.CreateEntity(Farm, 1, Vector2D(6, 6))
scheduler.CreateEntity(Farm, 3, Vector2D(8, 6))
scheduler.CreateEntity(Farm, 2, Vector2D(6, 8))
scheduler.CreateEntity(Farm, 4, Vector2D(8, 8))

scheduler.Schedule(0, constants.ROUNDS)

out = Output()
for time in xrange(0, constants.ROUNDS, Calculate(hours=1)):
#    for entity in World.entities[time]:
#        entity.Get(time, "Position")

#    World.entities[time][0].Get(time, "Position")
    #out.console(time)
    #sleep(constants.SLEEP_TIME)
    pass


print
#print len(json.dumps(World.entities, cls=ObjectEncoder))


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


