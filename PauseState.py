import GameState
import pygame

class PauseState(GameState.GameState):
    def __init__(self, game):
        self.name = "paused"
        self.game = game

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.ContinuePlaying()
