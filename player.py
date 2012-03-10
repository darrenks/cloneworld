'''
@authors: Richard B. Johnson
'''
from entity import Entity, Action
from utility import *

class Player(Entity):
    def __init__(self, x=0, y=0, f=Action.South):
        Entity.__init__(x, y, f)
        self.nextAction = Action.Wait
        
        # store player statistics
        self.moves = 0
        
        if debug.active: print self
        
    def setNextAction(self, action):
        self.nextAction = action
        
    def getNextMove(self, isWall):
        x, y = self.getNextStep(self.nextAction)
        
        self.setFacing(self.nextAction)
        self.nextAction = Action.Wait
        
        if (isWall(x, y) == True):
            return self.X, self.Y
        
        return x, y
        
    def __str__(self):
        s = "Player Information:\n"
        s += Entity.__str__(self)
        s += "%s %s\n"%(col("Next Action"), Action.toStr(self.nextAction))
        s += "%s %i\n"%(col("Moves"), self.moves)
        return s
    
    