import GameState
import pygame
import Button

class PauseState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game, "paused")
        continue_button = Button.ContinueGameButton(self.game)
        continue_button.SetPosition(self.game.screen_width/2 - continue_button.rect.width/2,
                                        (self.game.screen_height/2 - continue_button.rect.height/2) - 50)
        exit_button = Button.ExitToLevelSelect(self.game)
        exit_button.SetPosition(self.game.screen_width/2 - exit_button.rect.width/2,
                                    (self.game.screen_height/2 - exit_button.rect.height/2) + 50)

        self.buttons = [continue_button, exit_button]

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
                elif event.key == pygame.K_ESCAPE:
                    self.game.ContinuePlaying()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hovered:
                        button.Clicked()

    def Update(self):
        self.GetMousePos()
        for button in self.buttons:
            button.Update(self.mouse_pos)

    def DrawScreen(self):
        for button in self.buttons:
            self.game.screen.blit(button.image, button.rect)
