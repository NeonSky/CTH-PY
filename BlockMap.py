from Shape import Shape
from Block import Block

class BlockMap:
    #y, x
    blocks = {}

    def __init__(self):
        default_color = (0, 0, 0)

        for i in range(0, 20, 1):
            self.blocks[i] = (Block((0*Block.width, i*Block.width), default_color),
                              Block((1*Block.width, i*Block.width), default_color),
                              Block((2*Block.width, i*Block.width), default_color),
                              Block((3*Block.width, i*Block.width), default_color),
                              Block((4*Block.width, i*Block.width), default_color),
                              Block((5*Block.width, i*Block.width), default_color),
                              Block((6*Block.width, i*Block.width), default_color),
                              Block((7*Block.width, i*Block.width), default_color),
                              Block((8*Block.width, i*Block.width), default_color),
                              Block((9*Block.width, i*Block.width), default_color))

        self.blocks[10][0].applyBlock(Block((0, 0), (255, 0, 100)))

    def applyShape(self, shape):
        for block in shape:
            self.blocks[block.pos[1]/Block.width][block.pos[0]].applyBlock(block)


    def collides(self, shape, x_change, y_change):
        for block in shape.blocks:
            if(self.blocks[(y_change+block.pos[1])/Block.width][(x_change+block.pos[0])/Block.width].active()):
                return True
        return False


    def draw(self, screen):
        for blockRow in self.blocks:
            for block in self.blocks[blockRow]:
                block.draw(screen)
