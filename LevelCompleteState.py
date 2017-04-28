import pygame
import GameState

class LevelCompleteState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game, "levelcomplete")
        self.level_complete_image_1 = pygame.image.load("Resources/LevelCompletePart1.png").convert_alpha()
        self.level_complete_image_2 = pygame.image.load("Resources/LevelCompletePart2.png").convert_alpha()

    def Update(self):
        if not pygame.mixer.get_busy():
            self.game.GoToLevelSelect()

    def DrawScreen(self):
        self.game.screen.blit(self.level_complete_image_1, (self.game.screen_width / 2 - self.level_complete_image_1.get_width() / 2,
                                                          self.game.screen_height / 2 - self.level_complete_image_1.get_height() / 2 - 50))
        self.game.screen.blit(self.level_complete_image_2, (self.game.screen_width / 2 - self.level_complete_image_2.get_width() / 2,
                                                          self.game.screen_height / 2 - self.level_complete_image_2.get_height() / 2 + 50))
