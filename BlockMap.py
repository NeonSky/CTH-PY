from Shape import Shape

class BlockMap:
    blocks = {}

    def __init__(self):
        for i in range(0, 20, 1):
            self.blocks[i] = (False, False, False, False, False, False, False, False, False)

    def collides(self, shape, x_change, y_change):
        return True

    def draw(self):
        print("Draw BlockMap")