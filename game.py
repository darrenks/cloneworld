'''
@authors: Richard B. Johnson
'''
from level import *
from utility import *

import time

class Game:
    def __init__(self, interval = 200, path=""):
        self.reset()
        self.interval = interval
        
        if (len(path) > 0):
            self.loadPackageData(path)
        
    def reset(self):
        self.active = False
        self.totalscore = 0
        self.resetPackageData()
        
    def resetPackageData(self):
        self.datafile = ""
        self.levels = 0
        self.level = None
        
    def loadPackageData(self, path):
        file = None
        
        try:
            # load the header information
            file = open(path, "rb")
            self.datafile = path
            #self.levels = 0
        except IOError as e:
            debug.error(e)
        finally:
            if (file != None):
                file.close()
        
    def nextLevel(self):
        try:
            if (self.level != None):
                nxtlvl = self.level.ID + 1
            else:
                nxtlvl = 0
            
            self.level = Level(self.datafile, nxtlvl)
        except IOError:
            debug.error("Unable to locate '%s'."%(self.datafile))
            self.resetPackageData()
        except InvalidLevel:
            debug.notify("All levels have been completed.")
        
    def randomLevel(self):
        try:
            nxtlvl = random.randint(0, self.levels)
            self.level = Level(self.datafile, nxtlvl)
        except IOError:
            debug.error("Unable to locate '%s'."%(self.datafile))
            self.resetPackageData()
        
    def update(self):
        if (self.active == False):
            return False
        
        self.level.tick()
        time.sleep(self.interval / 1000.0)
        
        return True
    