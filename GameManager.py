from BlockMap import BlockMap
from Shape import Shape

class GameManager:
    blockMap = BlockMap()
    currentShape = Shape()

    def __init__(self):
        print("hej")

    def draw(self, screen):
        self.blockMap.draw(screen)
        self.shape.draw(screen)