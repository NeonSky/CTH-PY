from Shape import Shape
from Block import Block

class BlockMap:
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

    def collides(self, shape, x_change, y_change):
        return True

    def draw(self, screen):
        for blockRow in self.blocks:
            for block in self.blocks[blockRow]:
                block.draw(screen)
