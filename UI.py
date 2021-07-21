import pygame
from pygame.locals import *
def draw_board(game,screen):
    border_line=Rect(int(0.3*x),int(0.1*y),int(0.4*x),int(0.8*y))
    for i in range(game.x+1):
        pygame.draw.line(screen,Color(45,45,45),(left+grid_size*i,up),(left+grid_size*i,up+game.y*grid_size),width=2)
    for i in range(game.y+1):
        pygame.draw.line(screen,Color(45,45,45),(left,up+grid_size*i),(left+grid_size*game.x,up+grid_size*i),width=2)

def draw_border(game,screen):
    for i in range(game.x+2):
        tempRect=Rect(left+(grid_size)*(i-1),up-grid_size,grid_size-1,grid_size-1)
        pygame.draw.rect(screen,Color(255,100,100),tempRect,width=2)
        screen.fill(Color(100,255,100),tempRect)
        tempRect=Rect(left+(grid_size)*(i-1),up+grid_size*(game.y),grid_size-1,grid_size-1)
        pygame.draw.rect(screen,Color(255,100,100),tempRect,width=2)
        screen.fill(Color(100,255,100),tempRect)
    for i in range(game.y):
        tempRect=Rect(left-grid_size,up+(grid_size)*(i),grid_size-1,grid_size-1)
        pygame.draw.rect(screen,Color(255,100,100),tempRect,width=2)
        screen.fill(Color(100,255,100),tempRect)
        tempRect=Rect(left+grid_size*game.x,up+(grid_size)*(i),grid_size-1,grid_size-1)
        pygame.draw.rect(screen,Color(255,100,100),tempRect,width=2)
        screen.fill(Color(100,255,100),tempRect)
        
def draw_blocks(game,screen):
    for i in range(game.y):
        for j in range(game.x):
            tempRect=Rect(left+(grid_size)*j,up+grid_size*i,grid_size-1,grid_size-1)
            temp=game.board[i][j]
            pygame.draw.rect(screen,game.colors[temp],tempRect)
            

def draw(game,screen):
    global x,y,left,up,width,height,grid_size
    (x,y)=screen.get_size()
    left,up,width,height=int(0.3*x),int(0.1*y),int(0.4*x),int(0.8*y)
    grid_size=min(width//game.x,height//game.y)
    draw_board(game,screen)
    draw_border(game,screen)
    draw_blocks(game,screen)
    
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode(size)
    while running:
        pass
    
