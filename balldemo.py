import sys
import pygame

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

ballDemo(800, 640)
