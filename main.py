import sys

from direction import Direction
from level import Level
from game import Game

def sandbox():
    game = Game()
    game.level = Level()
    pid = game.level.setPlayer(5, 6, Direction.S)
    mid = game.level.addMonster("ball", 12, 7, Direction.E)
    # NO RELATION TO THE BALL DEMO
    
    print game.level.monsters[mid].brief()
    
    for i in range(0, 20):
        game.update()
        print game.level.monsters[mid].brief()
        
    print "\n", game.level.monsters[mid]

def main(argv):
    sandbox()
    
if __name__ == "__main__":
    main(sys.argv[1:])
