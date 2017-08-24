from Block import Block


class Shape:
    types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z', 'SMURF']
    type = types[0]
    color_i = (0, 255, 255)
    color_j = (0, 0, 255)
    color_l = (255, 165, 0)
    color_o = (255, 255, 0)
    color_s = (0, 255, 0)
    color_t = (170, 0, 255)
    color_z = (255, 0, 0)

    def __init__(self, pos, type, block_map):
        self.pos = pos
        self.type = type
        self.block_map=block_map
        self.createBlocks()

    def createBlocks(self):
        self.blocks = []
        if self.type == 'I':
            self.blocks.append(self.create_block(0, 0, self.color_i))
            self.blocks.append(self.create_block(1, 0, self.color_i))
            self.blocks.append(self.create_block(2, 0, self.color_i))
            self.blocks.append(self.create_block(3, 0, self.color_i))
        elif self.type == 'J':
            self.blocks.append(self.create_block(0, 0, self.color_j))
            self.blocks.append(self.create_block(1, 0, self.color_j))
            self.blocks.append(self.create_block(2, 0, self.color_j))
            self.blocks.append(self.create_block(2, 1, self.color_j))
        elif self.type == 'L':
            self.blocks.append(self.create_block(0, 0, self.color_l))
            self.blocks.append(self.create_block(1, 0, self.color_l))
            self.blocks.append(self.create_block(2, 0, self.color_l))
            self.blocks.append(self.create_block(0, 1, self.color_l))
        elif self.type == 'O':
            self.blocks.append(self.create_block(0, 0, self.color_o))
            self.blocks.append(self.create_block(1, 0, self.color_o))
            self.blocks.append(self.create_block(0, 1, self.color_o))
            self.blocks.append(self.create_block(1, 1, self.color_o))
        elif self.type == 'S':
            self.blocks.append(self.create_block(2, 0, self.color_s))
            self.blocks.append(self.create_block(1, 0, self.color_s))
            self.blocks.append(self.create_block(0, 1, self.color_s))
            self.blocks.append(self.create_block(1, 1, self.color_s))
        elif self.type == 'T':
            self.blocks.append(self.create_block(0, 0, self.color_t))
            self.blocks.append(self.create_block(1, 0, self.color_t))
            self.blocks.append(self.create_block(2, 0, self.color_t))
            self.blocks.append(self.create_block(1, 1, self.color_t))
        elif self.type == 'Z':
            self.blocks.append(self.create_block(0, 0, self.color_z))
            self.blocks.append(self.create_block(1, 0, self.color_z))
            self.blocks.append(self.create_block(1, 1, self.color_z))
            self.blocks.append(self.create_block(2, 1, self.color_z))
        elif self.type == 'SMURF':
            rc = (170, 47, 76)  # red color
            drc = (146, 48, 73)  # dark red color
            bc = (60, 144, 190)  # blue color
            dbc = (57, 125, 160)  # dark blue color
            gc = (224, 224, 224)  # grey color
            dgc = (51, 51, 51)  # dark grey color
            nc = False  # no color (black)

            blockColors = [
                [nc, nc, nc, rc, rc, rc, rc, rc],
                [nc, nc, rc, rc, rc, drc, drc],
                [nc, rc, rc, rc, drc, rc, rc, rc, rc],
                [nc, rc, rc, rc, rc, bc, gc, dgc],
                [nc, rc, bc, bc, gc, bc, gc, dgc, bc, bc],
                [nc, nc, bc, bc, gc, bc, bc, gc, gc, bc],
                [nc, nc, nc, dbc, gc, gc, gc, dbc],
                [nc, bc, bc, bc, dbc, gc, gc, gc, dbc],
                [bc, bc, nc, bc, bc, bc, gc, gc, gc, gc],
                [bc, bc, nc, rc, rc, rc, rc, nc, bc, bc],
                [nc, rc, rc, rc, nc, nc, rc, rc, rc],
                [nc, rc, rc, rc, nc, nc, rc, rc, rc]
            ]

            x = 0
            y = 0
            for blockColorsRow in blockColors:
                for blockColor in blockColorsRow:
                    if blockColor:
                        self.blocks.append(self.create_block(x, y, blockColor))
                    x += 1
                x = 0
                y += 1

    def move(self, (dx, dy)):
        self.shape_apply((lambda pos: pos[0]+dx*Block.width), (lambda pos: pos[1]+dy*Block.width))

    def horizontal_flip(self):
        bounds = self.get_shape_bounds()
        self.shape_apply((lambda pos: bounds[0][0] + bounds[0][1] - pos[0]), (lambda pos: pos[1]))

    def vertical_flip(self):
        bounds = self.get_shape_bounds()
        self.shape_apply((lambda pos: pos[0]), (lambda pos: bounds[1][0] + bounds[1][1] - pos[1]))

    def rotate(self, direction):  # true=clockwise, false=counter-clockwise
        bounds = self.get_shape_bounds()
        if direction:  # clockwise
            # x =  x.min_bound - y,  y = y.max_bound + x
            self.shape_apply((lambda pos: bounds[0][1] - (pos[1]-bounds[1][0])), (lambda pos: bounds[1][0] + (pos[0]-bounds[0][0])))
        else:  # counter-clockwise
            # x = x.max_bound + y,  y = y.max_bound - x
            self.shape_apply((lambda pos: bounds[0][0] + (pos[1]-bounds[1][0])), (lambda pos: bounds[1][1] - (pos[0]-bounds[0][0])))

    def shape_apply(self, x_func, y_func):
        for block in self.blocks:
            x_index=x_func(block.pos)/Block.width
            y_index=y_func(block.pos)/Block.width

            if not 0 <= x_index < self.block_map.width:
                return
            if not 0 <= y_index < self.block_map.height:
                return
            if self.block_map.blocks[y_index][x_index].active():
                return
        for block in self.blocks:
            block.pos = (x_func(block.pos), y_func(block.pos))

    def get_shape_bounds(self):
        block_x_values = map(lambda x: x.pos[0], self.blocks)
        max_x = max(block_x_values)
        min_x = min(block_x_values)
        block_y_values = map(lambda x: x.pos[1], self.blocks)
        max_y = max(block_y_values)
        min_y = min(block_y_values)
        return (min_x, max_x), (min_y, max_y)

    def fall(self):
        self.move((0, 1))

    def create_block(self, x_offset, y_offset, color):
        return Block((self.pos[0] + Block.width * x_offset, self.pos[1] + Block.width * y_offset), color)

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
