from random import randint

from BlockMap import BlockMap
from Shape import Shape
from Block import Block

class GameManager:
    blockMap = BlockMap()
    smurf_shape = Shape((0, 0), 'SMURF')

    def __init__(self):
        print("Game starting...")
        #self.spawn_shape()

    def spawn_shape(self):
        self.currentShape = Shape((0, 0), Shape.types[randint(0, len(Shape.types)-1)])

    fallTime = 30
    fallTimer = 0
    def update(self):
        if self.fallTimer >= self.fallTime:
            #self.smurf_shape.fall()
            self.fallTimer = 0
            #if not self.blockMap.collides(self.currentShape,0,Block.width):
             #   pass
                #self.currentShape.fall()
            return
        self.fallTimer += 1

    def draw(self, screen):
        self.blockMap.draw(screen)
        self.smurf_shape.draw(screen)
        #self.currentShape.draw(screen)