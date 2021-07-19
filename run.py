import pygame
from UI import *
from pygame.locals import *
from board import *


if __name__ == "__main__" :
    pygame.init()
    game=new_game()
    a=pygame.display.set_mode((1000,700))
    while(1):
        draw(game,a)
        pygame.display.flip()
        #event()
        
        
