import pygame
import GameState
import Button

class StartMenuState(GameState.GameState):
    def __init__(self, game):
        self.name = "startmenu"
        self.game = game
        start = Button.StartGameButton()
        start.SetPosition(game.screen_width / 2 - start.rect.width /2,
                          game.screen_height / 2 - start.rect.height / 2)
        self.buttons = [start]
        self.mouse_pos = None

    def HandleEvents(self, game):  # Handle events such as exiting and certain key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hovered:
                        button.Clicked(game)

    def Update(self): # Update GUI
        self.mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.Update(self.mouse_pos)

    def DrawScreen(self, screen):  # Draw buttons and background
        for button in self.buttons:
            screen.blit(button.image, button.rect)
