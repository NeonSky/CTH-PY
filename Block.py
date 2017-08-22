import pygame as pg

class Block:
    width = 32
    pos = (0, 0)
    size = (width, width)
    color = (0, 0, 0)
    edge_color = (255, 255, 255)
    edge_width = 1

    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.pos, self.size))
        pg.draw.rect(screen, self.edge_color, (self.pos, self.size), self.edge_width)

    def applyBlock(self, block):
        self.color = block.color

    def reset(self):
        self.color = (0, 0, 0)

    def active(self):
        return self.color != (0, 0, 0)