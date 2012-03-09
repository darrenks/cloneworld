import sys
import pygame

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

def ballDemo(width, height):
    pygame.init()
    
    speed = [2, 2]
    black = 0, 0, 0
    
    ball = pygame.image.load("../res/ball.gif")
    ballrect = ball.get_rect()
    
    screen = pygame.display.set_mode([width, height])
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

def main(argv):
    sandbox()
    ballDemo(800, 640)
    
if __name__ == "__main__":
    main(sys.argv[1:])
