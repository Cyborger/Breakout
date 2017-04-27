import pygame
import Spritesheet

class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, scale = 3):
        self.spritesheet = Spritesheet.Spritesheet(image_path, 1, 2, scale)
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

class LevelSelectButton(Button):
    def __init__(self, game, image_path, level):
        super().__init__(image_path, 2)
        self.game = game
        self.level = level

    def Clicked(self):
        self.game.ChooseLevel(self.level)

class StartGameButton(Button):
    def __init__(self, game):
        super().__init__("Resources/Buttons/StartButton.png")
        self.game = game

    def Clicked(self):  # Set game state to playing
        self.game.GoToLevelSelect()

class ExitGameButton(Button):
    def __init__(self, game):
        super().__init__("Resources/Buttons/ExitButton.png")
        self.game = game

    def Clicked(self):  # Set game running to false
        self.game.running = False

class ExitToLevelSelect(Button):
    def __init__(self, game):
        super().__init__("Resources/Buttons/ExitButton.png")
        self.game = game

    def Clicked(self):
        self.game.GoToLevelSelect()

class ContinueGameButton(Button):
    def __init__(self, game):
        super().__init__("Resources/Buttons/ContinueButton.png")
        self.game = game

    def Clicked(self):  # Set game state back to playing
        self.game.ContinuePlaying()

class BackButton(Button):
    def __init__(self, game):
        super().__init__("Resources/Buttons/BackButton.png", 2)
        self.game = game

    def Clicked(self):
        self.game.Start()
