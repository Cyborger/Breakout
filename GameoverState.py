import GameState
import pygame

class GameoverState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game, "gameover")
        self.gameover_image = pygame.image.load("Resources/GameOverScreen.png").convert_alpha()

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
                else:
                    self.game.Start()

    def Update(self):
        if not pygame.mixer.get_busy():
            self.game.GoToLevelSelect()

    def DrawScreen(self):
        self.game.screen.blit(self.gameover_image, (self.game.screen_width / 2 - self.gameover_image.get_width() / 2,
                                                    self.game.screen_height / 2 - self.gameover_image.get_height() / 2))
