from Shape import Shape
from Block import Block

class BlockMap:
    blocks = {}

    def __init__(self):
        default_color = (255, 0, 0)

        for i in range(0, 20, 1):
            self.blocks[i] = (Block((0, i), default_color),
                              Block((1, i), default_color),
                              Block((2, i), default_color),
                              Block((3, i), default_color),
                              Block((4, i), default_color),
                              Block((5, i), default_color),
                              Block((6, i), default_color),
                              Block((7, i), default_color),
                              Block((8, i), default_color),
                              Block((9, i), default_color))

    def collides(self, shape, x_change, y_change):
        return True

    def draw(self, screen):
        for blockRow in self.blocks:
            for block in self.blocks[blockRow]:
                block.draw(screen)
