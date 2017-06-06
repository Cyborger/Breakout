import pygame

class Spritesheet:
    def __init__(self, image_path, tiles_wide, tiles_high, scale = 1):
        self.image = pygame.image.load(image_path).convert_alpha()
        if scale != 1:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale,
                                                             self.image.get_height() * scale))
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.image.get_width() / self.tiles_wide
        self.tile_height = self.image.get_height() / self.tiles_high

    def GetImage(self, x, y):
        new_image = self.image.subsurface((x * self.tile_width, y * self.tile_height,
                                           self.tile_width, self.tile_height))
        return new_image
