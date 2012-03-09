'''
@authors: Richard B. Johnson
'''

class Action:
    __nextStep = [[0,-1], [1, 0], [0, 1], [-1, 0], [0, 0]]
    __dirStr = ["north", "east", "south", "west", "wait"]

    North = 0
    East  = 1
    South = 2
    West  = 3
    Wait  = -1
    
    @staticmethod
    def turnLeft(d):
        return (d - 1) & 3
    
    @staticmethod
    def turnRight(d):
        return (d + 1) & 3
    
    @staticmethod
    def turnAround(d):
        return (d + 2) & 3
    
    @staticmethod
    def nextStep(d):
        return Action.__nextStep[d]
        
    @staticmethod
    def toStr(d):
        return Action.__dirStr[d]
    