import pygame
from pygame.locals import *
def event():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print('up')
            if event.key == pygame.K_DOWN:
                print('down')
            if event.key == pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('right')

if __name__ == "__main__" :
    pygame.init()
    a= pygame.display.set_mode((600,400))
    while(1):
        event()
        
        
