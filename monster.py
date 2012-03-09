'''
@authors: Richard B. Johnson
'''
from entity import Entity, Direction
from utility import *

class Monster(Entity):
    pattern = {}
    
    def __init__(self, type, x=0, y=0, f=Direction.S):
        Entity.__init__(x, y, f)
        self.type = type
         
        if debug.active: print self        
        
    def standStill(self, isWall):
        return self.X, self.Y
    
    def moveBackAndForth(self, isWall):
        x, y = self.getNextStep()
        
        if (isWall(x, y) == True):
            self.turnAround()
            x, y = self.getNextStep()
            
            if (isWall(x, y) == True):
                return self.standStill(isWall)
                    
        return x, y
    
    pattern["ball"] = moveBackAndForth
    pattern["bat"]  = standStill
    pattern["ant"]  = standStill
    pattern["ship"] = standStill
    
    def getNextMove(self, isWall):
        nextMove = Monster.pattern[self.type]
        return nextMove(self, isWall)
    
    def __str__(self):
        s = "Monster Information:\n"
        s += Entity.__str__(self)
        s += "%s %s\n"%(col("Type"), self.type)
        return s
    
    def brief(self):
        return Entity.brief(self) + ", %s"%(self.type)
    
    