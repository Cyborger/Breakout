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
            if layer.name == "Blue Blocks":
                for x, y, image in layer.tiles():
                    new_block = Block.BlueBlock(x * tile_width, y * tile_height)
                    self.all_blocks.append(new_block)

    def RemoveDestroyedBlocks(self):
        for block in self.blocks:
            if block.broken:
                self.blocks.remove(block)

    def ResetLevel(self):
        self.blocks = copy.copy(self.all_blocks)
