import pygame
import Spritesheet

class Button(pygame.sprite.Sprite):
    def __init__(self, image_path):
        self.spritesheet = Spritesheet.Spritesheet(image_path, 1, 2, 4)
        self.not_hovered_image = self.spritesheet.GetImage(0, 0)
        self.hovered_image = self.spritesheet.GetImage(0, 1)
        self.image = self.not_hovered_image.copy()
        self.rect = self.image.get_rect()
        self.hovered = False

    def Update(self, mouse_pos):  # Update image
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.Hovered()
        else:
            if self.hovered:
                self.NotHovered()

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def Hovered(self):  # Change image if mouse is hovering
        self.image = self.hovered_image.copy()
        self.hovered = True

    def NotHovered(self):  # Set image back to default if not Hovered
        self.image = self.not_hovered_image.copy()
        self.hovered = False

    def Clicked(self):  # Overwritten by subclasses
        pass

class StartGameButton(Button):
    def __init__(self):
        super().__init__("Resources/StartButton.png")

    def Clicked(self, game):  # Set game state to playing
        game.StartPlaying()

class ExitGameButton(Button):
    def __init__(self):
        pass

    def Clicked(self, game):  # Set game running to false
        game.running = False

class ContinueGameButton(Button):
    def __init__(self):
        pass

    def Clicked(self, game):  # Set game state back to playing
        game.ContinuePlaying()
