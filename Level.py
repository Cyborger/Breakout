import pytmx
import Block
import copy

class Level:
    def __init__(self, tmx_path):
        self.tmx = pytmx.load_pygame(tmx_path)
        self.all_blocks = []
        self.blocks = []
        self.width = self.tmx.width * self.tmx.tilewidth
        self.height = self.tmx.height * self.tmx.tileheight
        self.CreateLevel()

    def CreateLevel(self):  # Use the tmx path
        tile_width = self.tmx.tilewidth
        tile_height = self.tmx.tileheight
        for layer in self.tmx.layers:
            for x, y, image in layer.tiles():
                type_of_block = self.tmx.get_tile_properties(x, y, self.tmx.layers.index(layer))["Type"]
                if type_of_block == "Blue":
                    new_block = Block.BlueBlock(x * tile_width, y * tile_height)
                    self.all_blocks.append(new_block)
                elif type_of_block == "Orange":
                    new_block = Block.OrangeBlock(x * tile_width, y * tile_height)
                    self.all_blocks.append(new_block)

    def UpdateBlocks(self):
        for block in self.blocks:
            block.Update()
            if block.broken:
                self.blocks.remove(block)

    def ResetLevel(self):
        self.blocks = self.all_blocks[:]
        for block in self.blocks:
            block.Reset()
