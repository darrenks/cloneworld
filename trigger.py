'''
@authors: Richard B. Johnson
'''
from entity import Entity, Action
from utility import *

class Trigger(Entity):
    def __init__(self, x=0, y=0, f=Action.South):
        Entity.__init__(x, y, f)
        
        if debug.active: print self        
        
    def update(self):
        return True
    
    def __str__(self):
        s = "Trigger Information:\n"
        s += Entity.__str__(self)
        return s
    