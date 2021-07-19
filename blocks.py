import random
class blocks:
    def __init__(self):
        self.tetriminos=[[1, 1, 1, 1], [[2, 0, 0], [2, 2, 2]], [[0, 0, 3], [3, 3, 3]], [[4, 4], [4, 4]], [[0, 5, 5], [5, 5, 0]], [[0, 6, 0], [6, 6, 6]], [[7, 7, 0], [0, 7, 7]]]
        self.blocks=[random.randint(0,7) for _ in range(3)]
        self.hold_block=0
        self.falling=0
        
    def new(self):int
        self.blocks.append(random.randint(0,7))
        return self.blocks.pop(0)
    
    def hold(self):
        if self.hold_block==0:
            self.hold_block=self.falling
            self.falling=self.new()
        else:
            self.hold_block,self.falling=self.falling,self.hold_block
            
