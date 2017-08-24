from Block import Block

class BlockMap:

    width = 10
    height = 20

    def __init__(self):
        self.empty_map()

    def empty_map(self):
        # y, x
        self.blocks = {}
        self.default_color = (0, 0, 0)

        for i in range(0, 20, 1):
            self.blocks[i] = (Block((0 * Block.width, i * Block.width), default_color),
                              Block((1 * Block.width, i * Block.width), default_color),
                              Block((2 * Block.width, i * Block.width), default_color),
                              Block((3 * Block.width, i * Block.width), default_color),
                              Block((4 * Block.width, i * Block.width), default_color),
                              Block((5 * Block.width, i * Block.width), default_color),
                              Block((6 * Block.width, i * Block.width), default_color),
                              Block((7 * Block.width, i * Block.width), default_color),
                              Block((8 * Block.width, i * Block.width), default_color),
                              Block((9 * Block.width, i * Block.width), default_color))

        self.blocks[10][0].applyBlock(Block((0, 0), (255, 0, 100)))

    def applyShape(self, shape):
        for block in shape.blocks:
            if not self.is_outside(block.pos):
                self.blocks[block.pos[1]/Block.width][block.pos[0]/Block.width].applyBlock(block)
        self.check_rows()


    def collides(self, shape, x_change, y_change):
        for block in shape.blocks:
            x_coord = (x_change+block.pos[0])/Block.width
            y_coord = (y_change+block.pos[1])/Block.width
            if self.is_outside((x_coord, y_coord)):
                return True

            if(self.blocks[y_coord][x_coord].active()):
                return True
        return False

    def check_rows(self):
        for blockRow in self.blocks:
            isRowFull = True
            for block in self.blocks[blockRow]:
                isRowFull = False
                break
            if isRowFull:
                for block in self.blocks[blockRow]:
                    block = Block(block.pos, self.default_color)


    def is_outside(self, coord):
        if coord[0] < 0 or coord[0] >= self.width:
            return True
        if coord[1] < 0 or coord[1] >= self.height:
            return True
        return False


    def draw(self, screen):
        for blockRow in self.blocks:
            for block in self.blocks[blockRow]:
                block.draw(screen)
