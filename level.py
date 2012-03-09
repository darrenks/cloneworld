'''
@authors: Richard B. Johnson
'''
from player import Player
from monster import Monster
from trigger import Trigger
from utility import *

class Level:
    def __init__(self, path="", lvlnum=0):
        self.reset()
        
        if (len(path) > 0):
            self.load(path, lvlnum)
        
    def reset(self):
        self.ticks = 0
        self.tiles = []
        self.description = ""
        self.triggers = {}
        self.monsters = {}
        self.player = None
        self.time = 0
        self.ID = -1
        
    def load(self, path, lvlnum):
        debug.notify("Loading level %i from '%s'."%(lvlnum, path))
        
        file = open(path, 'rb')
        file.readlines()
        # ...
        
        # when out of levels:
        # raise InvalidLevel
        
        file.close()
        
        self.ID = lvlnum
        
    def setPlayer(self, x, y, f):
        debug.notify("Setting up player.")
        self.player = Player(x, y, f)
        return self.player.ID
        
    def addMonster(self, type, x, y, f):
        debug.notify("Adding a new monster.")
        m = Monster(type, x, y ,f)
        self.monsters[m.ID] = m
        return m.ID
        
    def addTrigger(self, t):
        debug.notify("Adding a new trigger.")
        self.triggers[t.ID] = t
        return t.ID
    
    def isWall(self, x, y):
        return self.dummyIsWall(x, y)
        
    def dummyIsWall(self, x, y):
        return (random.randint(0, 5) == 0)
    
    def isDeathTile(self, x, y):
        return False
        #debug.raiseNotDefined()
        
    def updateMonsters(self):
        for id in self.monsters.keys():
            if (self.monsters[id].active == False):
                continue
            
            x, y = self.monsters[id].getNextMove(self.isWall)
            
            self.monsters[id].setLocation(x, y)
            
            if (self.isDeathTile(x, y) == True):
                self.monsters[id].setActive(False)
        
    def tick(self):
        self.updateMonsters()
        self.ticks += 1
        
    def briefLocations(self):
        s = ""
        
        if (self.player != None):
            s += "\nPlayer Location:\n"
            s += self.player.brief() + "\n"
        
        if (len(self.monsters.keys()) > 0):
            s += "\nMonster Locations:\n"
            
            for m in self.monsters.values():
                s += m.brief() + "\n"
    
        if (len(self.triggers.keys()) > 0):
            s += "\nTrigger Locations:\n"
            
            for t in self.triggers.values():
                s += t.brief() + "\n"
                
        return s
    
    def __str__(self):
        s = "Level Information:\n"
        s += "Ticks: %i\n"%(self.ticks)
        
        if (len(self.description) > 0):
            s += "Description:\n%s\n"%(self.description)
        
        s += self.briefLocations()
        return s
    

class InvalidLevel(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
