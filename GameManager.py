from BlockMap import BlockMap
from Shape import Shape

class GameManager:
    blockMap = BlockMap()
    currentShape = Shape((0, 0), 'Z')

    def __init__(self):
        print("Game starting...")

    fallTime = 30
    fallTimer = 0
    def update(self):
        if self.fallTimer >= self.fallTime:
            self.currentShape.fall()
            self.fallTimer = 0
            return
        self.fallTimer += 1

    def draw(self, screen):
        self.blockMap.draw(screen)
        self.currentShape.draw(screen)