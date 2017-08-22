from Block import Block

class Shape:
    pos = (0, 0)
    type = 'I' #I, O, T, S, Z, J, L
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
            self.blocks.append(Block(self.pos, self.color_i))
            self.blocks.append(Block((self.pos[0]+Block.width, self.pos[1]), self.color_i))
            self.blocks.append(Block((self.pos[0]+Block.width*2, self.pos[1]), self.color_i))
            self.blocks.append(Block((self.pos[0]+Block.width*3, self.pos[1]), self.color_i))
        elif self.type == 'J':
            self.blocks.append(Block(self.pos, self.color_j))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_j))
            self.blocks.append(Block((self.pos[0] + Block.width * 2, self.pos[1]), self.color_j))
            self.blocks.append(Block((self.pos[0] + Block.width * 2, self.pos[1] + Block.width), self.color_j))
        elif self.type == 'L':
            self.blocks.append(Block(self.pos, self.color_l))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_l))
            self.blocks.append(Block((self.pos[0] + Block.width * 2, self.pos[1]), self.color_l))
            self.blocks.append(Block((self.pos[0], self.pos[1] + Block.width), self.color_l))
        elif self.type == 'O':
            self.blocks.append(Block(self.pos, self.color_o))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_o))
            self.blocks.append(Block((self.pos[0], self.pos[1] + Block.width), self.color_o))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1] + Block.width), self.color_o))
        elif self.type == 'S':
            self.blocks.append(Block((self.pos[0] + Block.width*2, self.pos[1]), self.color_s))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_s))
            self.blocks.append(Block((self.pos[0], self.pos[1] + Block.width), self.color_s))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1] + Block.width), self.color_s))
        elif self.type == 'T':
            self.blocks.append(Block(self.pos, self.color_t))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_t))
            self.blocks.append(Block((self.pos[0] + Block.width * 2, self.pos[1]), self.color_t))
            self.blocks.append(Block((self.pos[0] + Block.width , self.pos[1] + Block.width), self.color_t))
        elif self.type == 'Z':
            self.blocks.append(Block(self.pos, self.color_z))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1]), self.color_z))
            self.blocks.append(Block((self.pos[0] + Block.width, self.pos[1] + Block.width), self.color_z))
            self.blocks.append(Block((self.pos[0] + Block.width * 2, self.pos[1] + Block.width), self.color_z))



    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)