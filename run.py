import pygame
from UI import *
from pygame.locals import *
from game import *
from Events import *

if __name__ == "__main__" :
    pygame.init()
    crt_game=new_game()
    a=pygame.display.set_mode((1000,700))
    while(1):
        draw(crt_game,a)
        pygame.display.flip()
        pygame.time.delay(100)
        event()
        #crt_game.test()
        crt_game.tick()
        
        
