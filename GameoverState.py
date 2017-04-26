import GameState
import pygame

class GameoverState(GameState.GameState):
    def __init__(self, game):
        self.name = "gameover"
        self.game = game

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
                else:
                    self.game.Start()
