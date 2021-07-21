import random
import pygame
from pygame.locals import *
class new_game:
    def __init__(self,x=12,y=20,tetriminos=[[[1, 1, 1, 1],[0,0,0,0]], [[2, 0, 0], [2, 2, 2]], [[0, 0, 3], [3, 3, 3]], [[4, 4], [4, 4]], [[0, 5, 5], [5, 5, 0]], [[0, 6, 0], [6, 6, 6]], [[7, 7, 0], [0, 7, 7]]]):
        self.colors=[Color(149,160,166),Color(65,241,239),Color(13,23,235),Color(236,129,44),Color(230,229,57),Color(62,240,51),Color(156,20,235),Color(234,0,29)]
        self.tetriminos=tetriminos
        self.x,self.y=x,y
        self.board=[[0 for i in range(x)] for _ in range(y)]
        self.score=0
        self.combo=0
        self.holding=0
        self.falling=0
        self.blocks=[random.randint(0,7) for _ in range(3)]
        self.speed=1
        self.cord=0
        
    def tick(self):
        if self.falling:
            self.fall()
        else:
            self.blocks.append(random.randint(0,7))
            self.falling=self.blocks.pop(0)
            self.spawn(self.falling)

    def spawn(self,t):
        def over_lap(tx,ty,l):
            for i in range(ty):
                for j in range(tx):
                    if self.board[l+i][j] and self.tetriminos[i][j]:
                        return 1
            return 0
        tx,ty=(self.tetriminos[t][0]),len(self.tetriminos[t])
        l=(self.x-tx-1)//2   #left
        for i in range(self.x//2+1):
            a,b=l+i.l-i
            if not over_lap(x,a):
                c=a
            elif not over_lap(x,b):
                c=b
            else:
                c=0
            if c:
                for i in range(ty):
                    for j in range(tx):
                        self.board[i][c+j]=self.tetriminos[t][i][j]
                self.cord=(l,ty)
                return
        self.gg()                        
        
    def fall(self):
        def fix():
            for i in range(ty):
                for j in range(tx):
                    if self.board[self.cord[l+j]][self.card[2+i]]:
                        self.board=str(self.board)
        #check:
        for i in range(tx):
            if not self.board[self.cord[1]+1][l+i] and self.tetriminos[self.falling][-1][i]:
                fix()
                break
        for i in range(ty):
            for j in range(tx):
                if self.board:
                    pass
        
    def gg(self):
        pass
        
    def hold(self):
        if self.holding==0:
            self.holding=self.falling
            self.falling=self.new()
        else:
            self.holding,self.falling=self.falling,self.holding

    def eliminate(self):
        count=0
        for i in range(len(self.board)):
            for j in self.board[i]:
                if j==0:
                    break
            else:
                count+=1
                self.board=[[0 for i in range(12)]]+self.board[0:i][:]+self.board[i+1:][:]
        if count:
            if combo:
                self.score=2**(count-1)*100*1.5
            else:
                self.socre=2**(count-1)*100
                combo=1
        
    def __str__(self):
        s='[XXXXXXXXXXXX]\n'
        for i in self.board:
            s+='['
            for j in i:
                s+=str(j)
            s+=']\n'
        s+='[XXXXXXXXXXXX]'
        return s
    
if __name__=="__main__":
    temp=game()
    temp.board[2]=[1 for i in range(12)]
    print(temp)
    print()
    temp.board[3][2]=9
    temp.board[1][5]=1
    print(temp)
    print()
    temp.eliminate()
    print(temp)
