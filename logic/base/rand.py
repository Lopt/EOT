# -*- coding: utf-8 -*-

import random
import threading

'''
Hier passiert was böses... wenn zwei Threads ein random anfordern, aber im seed das ganze wechselt, wird das eine random mit dem seed des anderen verwendet
-> Inkonsitenz. Die Methoden müssten threadsafe sein
Ist das Lock zu Zeitaufwändig?
'''

class Random():
    seed_number = 0
    lock = threading.Lock()

    @staticmethod
    def _seed(entity, seed):
        random.seed(str(Random.seed_number + seed + entity.entropy))
    
    @staticmethod
    def choice(entity, choice, seed=0):
        with Random.lock:
            Random._seed(entity, seed)
            return random.choice(choice)

    @staticmethod    
    def random(entity, seed=0):
        with Random.lock:
            Random._seed(entity, seed)
            return random.random()
            
    @staticmethod 
    def randint(entity, start, stop, seed=0):
        with Random.lock:
            Random._seed(entity, seed)
            return random.randint(start, stop)
