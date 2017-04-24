import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)
        self.hits_needed = 0
        self.hits = 0
        self.broken = False

    def SetPosition(self, x, y):  # Set rect x and y
        self.rect.x = x
        self.rect.y = y

    def Break(self):  # Has been hit
        self.hits += 1
        if self.hits >= self.hits_needed:
            self.broken = True

class BlueBlock(Block):
    def __init__(self, x, y):
        super().__init__("Resources/BlueBlock.png", x, y)
        self.hits_needed = 1
