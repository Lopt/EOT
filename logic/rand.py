# -*- coding: utf-8 -*-

import random
import threading
from logic.world import World

'''
Hier passiert was böses... wenn zwei Threads ein random anfordern, aber im seed das ganze wechselt, wird das eine random mit dem seed des anderen verwendet
-> Inkonsitenz. Die Methoden müssten threadsafe sein
Ist das Lock zu Zeitaufwändig?
'''

class Random():
    lock = threading.Lock()

    @staticmethod
    def seed(entity):
        random.seed(str(entity.entropie) + str(World.time))
        entity.entropie += 1    
    
    @staticmethod
    def choice(entity, choice):
        with Random.lock:
            Random.seed(entity)
            return random.choice(choice)

    @staticmethod    
    def random(entity):
        with Random.lock:
            Random.seed(entity)
            return random.random()
            
    @staticmethod 
    def randint(entity, start, stop):
        with Random.lock:
            Random.seed(entity)        
            return random.randint(start, stop)
        
