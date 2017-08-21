import pygame as pg

class Block:
    pos = (0, 0)
    size = (32, 32)
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