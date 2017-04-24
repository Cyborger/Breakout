import pygame

class GameState:
    def __init__(self, game):
        self.game = game
        self.name = ""

    def HandleEvents(self):  # Handle events such as exiting and certain key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

    def Update(self):  # Update everything that needs to be updated
        pass

    def ClearScreen(self):  # Clear the screen for next draw
        self.game.screen.fill((0,0,0))  # Fill with black

    def DrawScreen(self):  # Draw everything
        pass

    def UpdateDisplay(self):
        pygame.display.flip()
