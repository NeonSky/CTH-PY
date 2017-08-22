from Block import Block

class Shape:
    pos = (0, 0)
    types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z', 'SMURF']
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
        elif self.type == 'SMURF':
            rc = (170, 47, 76) #red color
            drc = (146, 48, 73) #dard red color
            bc = (60,144,190) #blue color
            dbc = (57,125,160) #dark blue color
            gc = (224,224,224) #grey color
            dgc = (51,51,51) #dark grey color
            nc = (0,0,0) #no color (black)

            blockColors = [
                [nc,nc,nc,rc,rc,rc,rc,rc],
                [nc,nc,rc,rc,rc,drc,drc],
                [nc,rc,rc,rc,drc,rc,rc,rc,rc],
                [nc,rc,rc,rc,rc,bc,gc,dgc],
                [nc,rc,bc,bc,gc,bc,gc,dgc,bc,bc],
                [nc,nc,bc,bc,gc,bc,bc,gc,gc,bc],
                [nc,nc,nc,dbc,gc,gc,gc,dbc],
                [nc,bc,bc,bc,dbc,gc,gc,gc,dbc],
                [bc,bc,nc,bc,bc,bc,gc,gc,gc,gc],
                [bc,bc,nc,rc,rc,rc,rc,nc,bc,bc],
                [nc,rc,rc,rc,nc,nc,rc,rc,rc],
                [nc,rc,rc,rc,nc,nc,rc,rc,rc]
            ]

        x = 0
        y = 0
        for blockColorsRow in blockColors:
            for blockColor in blockColorsRow:
                self.blocks.append(self.create_block(x, y, blockColor))
                x += 1
            x = 0
            y += 1

    def fall(self):
        self.pos = (self.pos[0], self.pos[1] + Block.width)
        for block in self.blocks:
            block.pos = (block.pos[0], block.pos[1] + Block.width)

    def create_block(self, x_offset, y_offset, color):
        return Block((self.pos[0] + Block.width * x_offset, self.pos[1] + Block.width * y_offset), color)

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)