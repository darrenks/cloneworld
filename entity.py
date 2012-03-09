'''
@authors: Richard B. Johnson
'''
from abc import ABCMeta, abstractmethod
from action import Action
from utility import *

class Entity:
    __metaclass__ = ABCMeta
    __idCounter = 1
    
    @classmethod
    def __init__(self, x=0, y=0, f=Action.South):
        self.setLocation(x, y)
        self.startX = x
        self.startY = y
        self.facing = f
        self.active = True
        self.ID = Entity.__idCounter
        
        Entity.__idCounter += 1
        
    @classmethod
    def setActive(self, active):
        self.active = active
        
    @classmethod
    def setLocation(self, x, y):
        self.X = x
        self.Y = y
        
    @classmethod
    def setFacing(self, f):
        self.facing = f
        
    @classmethod
    def turnLeft(self):
        self.facing = Action.turnLeft(self.facing)
        
    @classmethod
    def turnRight(self):
        self.facing = Action.turnRight(self.facing)
        
    @classmethod
    def turnAround(self):
        self.facing = Action.turnAround(self.facing)

    @classmethod
    def getNextStep(self):
        x, y = Action.nextStep(self.facing)
        return self.X + x, self.Y + y
    
    @abstractmethod
    def getNextMove(self):
        debug.raiseNotDefined()
        
    def __str__(self):
        s =  "%s %i\n"%(col("Unique ID"), self.ID)
        s += "%s %i, %i\n"%(col("Start"), self.startX, self.startY)
        s += "%s %i, %i\n"%(col("Location"), self.X, self.Y)
        s += "%s %s\n"%(col("Facing"), Action.toStr(self.facing))
        t = "active" if self.active else "inactive"
        s += "%s %s\n"%(col("Status"), t)
        return s
    
    def brief(self):
        t = "active" if self.active else "inactive"
        return "ID %i, Loc (%i, %i), %s, %s"%(
            self.ID, self.X, self.Y, Action.toStr(self.facing), t)
        
    