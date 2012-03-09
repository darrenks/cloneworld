'''
@authors: Richard B. Johnson
'''

class Direction:
    __nextStep = [[0,-1], [1, 0], [0, 1], [-1, 0]]
    __dirStr = ["north", "east", "south", "west"]

    N = 0
    E = 1
    S = 2
    W = 3
    
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
        return Direction.__nextStep[d]
        
    @staticmethod
    def toStr(d):
        return Direction.__dirStr[d]
    