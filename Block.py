import pygame
import Timer
import Spritesheet

class Block(pygame.sprite.Sprite):
    def __init__(self, animation, x, y):
        self.animation = animation
        self.image = self.animation.GetImage(0, 0)
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)
        self.hits_needed = 0
        self.hits = 0
        self.break_timer = Timer.Timer(2)
        self.broken = False

    def SetPosition(self, x, y):  # Set rect x and y
        self.rect.x = x
        self.rect.y = y

    def Hit(self):  # Has been hit
        self.hits += 1
        if self.hits > self.animation.tiles_high - 1:
            self.hits = self.animation.tiles_high - 1
        self.image = self.animation.GetImage(0, self.hits)

    def Update(self):
        if self.hits >= self.hits_needed:
            self.break_timer.Update()
        if self.break_timer.complete:
            self.broken = True

    def Reset(self):
        self.image = self.animation.GetImage(0, 0)
        self.break_timer.Reset()
        self.hits = 0
        self.broken = False

class BlueBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/BlueBlock.png", 1, 2, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 1

class OrangeBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/OrangeBlock.png", 1, 3, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 2

class PurpleBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/PurpleBlock.png", 1, 4, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 3

class BlackBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/BlackBlock.png", 1, 5, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 4
