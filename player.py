'''
@authors: Richard B. Johnson
'''
from entity import Entity, Direction
from utility import *

class Player(Entity):
    def __init__(self, x=0, y=0, f=Direction.S):
        Entity.__init__(x, y, f)
        
        # store player statistics
        self.moves = 0
        
        if debug.active: print self
        
    def getNextMove(self):
        # may not need
        debug.raiseNotDefined()
        
    def __str__(self):
        s = "Player Information:\n"
        s += Entity.__str__(self)
        s += "%s %i\n"%(col("Moves"), self.moves)
        return s
    
    