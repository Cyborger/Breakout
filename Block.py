import pygame
import Timer
import Spritesheet

class Block(pygame.sprite.Sprite):
    def __init__(self, animation, x, y):
        self.animation = animation
        self.image = self.animation.GetImage(0, 0)
        self.rect = self.image.get_rect()
        self.broken_frames = []
        self.SetPosition(x, y)
        self.hits_needed = 0
        self.hits = 0
        self.break_timer = Timer.Timer(2)
        self.broken = False
        self.break_sound = pygame.mixer.Sound(file = "Resources/Music/Coin.wav")

    def GatherFrames(self, number_of_animations):
        for i in range(number_of_animations + 1):
            self.broken_frames.append(self.animation.GetImage(0, i))

    def SetPosition(self, x, y):  # Set rect x and y
        self.rect.x = x
        self.rect.y = y

    def Hit(self):  # Has been hit
        self.hits += 1
        if self.hits > len(self.broken_frames) - 1:
            self.hits = len(self.broken_frames) - 1
        self.image = self.broken_frames[self.hits]

    def Update(self):
        if self.hits >= self.hits_needed:
            if self.break_timer.current_passes == 0:
                self.break_sound.play()
            self.break_timer.Update()
        if self.break_timer.complete:
            self.broken = True

    def Reset(self):
        self.image = self.broken_frames[0]
        self.break_timer.Reset()
        self.hits = 0
        self.broken = False

class BlueBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/BlueBlock.png", 1, 2, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 1
        self.GatherFrames(self.hits_needed)

class OrangeBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/OrangeBlock.png", 1, 3, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 2
        self.GatherFrames(self.hits_needed)

class PurpleBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/PurpleBlock.png", 1, 4, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 3
        self.GatherFrames(self.hits_needed)

class BlackBlock(Block):
    def __init__(self, x, y):
        animation = Spritesheet.Spritesheet("Resources/Blocks/BlackBlock.png", 1, 5, 1)
        super().__init__(animation, x, y)
        self.hits_needed = 4
        self.GatherFrames(self.hits_needed)
