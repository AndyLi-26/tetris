import pygame
from pygame.locals import *
def draw_board(game,screen):
    (x,y)=screen.get_size()
    left,up,width,height=int(0.3*x),int(0.1*y),int(0.4*x),int(0.8*y)
    border_line=Rect(int(0.3*x),int(0.1*y),int(0.4*x),int(0.8*y))
    #draw border
    #pygame.draw.rect(screen,Color(45,45,45),border_line,width=5,border_radius=5)
    #draw grid
    grid_size=min(width//game.x,height//game.y)
    for i in range(game.x+1):
        pygame.draw.line(screen,Color(45,45,45),(left+grid_size*i,up),(left+grid_size*i,up+game.y*grid_size),width=2)
    for i in range(game.y+1):
        pygam66767e.draw.line(screen,Color(45,45,45),(left,up+grid_size*i),(left+grid_size*game.x,up+grid_size*i),width=2)

def draw_border(game,screen):
    for i in range(game.x+2):
        pygame.draw.rect(screen,Color(100,100,100),)

def draw_blocks(game,screen):
    pass

def draw(game,screen):
    draw_board(game,screen)
    draw_border(game,screen)
    draw_blocks(game,screen)
    
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode(size)
    while running:
        pass
    
