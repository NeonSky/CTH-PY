from Block import Block

class Shape:
    pos = (0, 0)
    types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    type = types[0]
    color_i = (0, 255, 255)
    color_j = (0, 0, 255)
    color_l = (255, 165, 0)
    color_o = (255, 255, 0)
    color_s = (0, 255, 0)
    color_t = (170, 0, 255)
    color_z = (255, 0, 0)
    blocks = []

    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.createBlocks()

    def createBlocks(self):
        if self.type == 'I':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(2, 0, self.color_z))
            self.blocks.append(self.create_block(3, 0, self.color_z))
        elif self.type == 'J':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(2, 0, self.color_z))
            self.blocks.append(self.create_block(2, 1, self.color_z))
        elif self.type == 'L':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(2, 0, self.color_z))
            self.blocks.append(self.create_block(0, 1, self.color_z))
        elif self.type == 'O':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(0, 1, self.color_z))
            self.blocks.append(self.create_block(1, 1, self.color_z))
        elif self.type == 'S':
            self.blocks.append(self.create_block(2, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(0, 1, self.color_z))
            self.blocks.append(self.create_block(1, 1, self.color_z))
        elif self.type == 'T':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(2, 0, self.color_z))
            self.blocks.append(self.create_block(1, 1, self.color_z))
        elif self.type == 'Z':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(1, 1, self.color_z))
            self.blocks.append(self.create_block(2, 1, self.color_z))

    def fall(self):
        self.pos = (self.pos[0], self.pos[1] + Block.width)
        for block in self.blocks:
            block.pos = (block.pos[0], block.pos[1] + Block.width)

    def create_block(self, x_offset, y_offset, color):
        return Block((self.pos[0] + Block.width * x_offset, self.pos[1] + Block.width * y_offset), color)

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)