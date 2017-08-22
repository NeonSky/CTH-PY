from BlockMap import BlockMap
from Shape import Shape

class GameManager:
    blockMap = BlockMap()
    currentShape = Shape((0, 0), 'I')

    def __init__(self):
        print("Game starting...")

    def draw(self, screen):
        self.blockMap.draw(screen)
        self.currentShape.draw(screen)