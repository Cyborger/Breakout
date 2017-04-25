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
                self.game.Start()
