from Block import Block

class Shape:
    pos = (0, 0)
    type = 'I' #I, O, T, S, Z, J, L
    blocks = []

    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.createBlocks()

    def createBlocks(self):
        if self.type == 'I':
            self.blocks.append(Block(self.pos, (0, 0, 255)))
            self.blocks.append(Block((self.pos[0]+32, self.pos[1]), (0, 0, 255)))
            self.blocks.append(Block((self.pos[0]+32*2, self.pos[1]), (0, 0, 255)))
            self.blocks.append(Block((self.pos[0]+32*3, self.pos[1]), (0, 0, 255)))
        elif type == 'O':
            self.blocks.append(Block(self.pos, (0, 0, 255)))
            self.blocks.append(Block(self.pos, (0, 0, 255)))
            self.blocks.append(Block(self.pos, (0, 0, 255)))
            self.blocks.append(Block(self.pos, (0, 0, 255)))


    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)