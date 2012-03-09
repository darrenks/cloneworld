import sys

from action import Action
from level import Level
from game import Game

CloneWorld = Game()

def load_level(path, lvlID = 1, format = None):
    return CloneWorld.level.load(path, lvlID)

def move_chip(action = Action.Wait):
    return
    
def sandbox():
    CloneWorld.level = Level()
    pid = CloneWorld.level.setPlayer(5, 6, Action.South)
    mid = CloneWorld.level.addMonster("ball", 12, 7, Action.East)
    # NO RELATION TO THE BALL DEMO
    
    print CloneWorld.level.monsters[mid].brief()
    
    for i in range(0, 20):
        CloneWorld.update()
        print CloneWorld.level.monsters[mid].brief()
        
    print "\n", CloneWorld.level.monsters[mid]

def main(argv):
    sandbox()
    
if __name__ == "__main__":
    main(sys.argv[1:])
