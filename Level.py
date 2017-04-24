import pytmx
import Block

class Level:
    def __init__(self, tmx_path):
        self.tmx = pytmx.load_pygame(tmx_path)
        self.blocks = []
        self.width = self.tmx.width * self.tmx.tilewidth
        self.height = self.tmx.height * self.tmx.tileheight

    def CreateLevel(self):  # Use the tmx path
        tile_width = self.tmx.tilewidth
        tile_height = self.tmx.tileheight
        for layer in self.tmx.layers:
            if layer.name == "Blue Blocks":
                for x, y, image in layer.tiles():
                    new_block = Block.BlueBlock(x * tile_width, y * tile_height)
                    self.blocks.append(new_block)

    def RemoveDestroyedBlocks(self):
        for block in self.blocks:
            if block.broken:
                self.blocks.remove(block)
