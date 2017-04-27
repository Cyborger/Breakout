import GameState
import Button
import pygame

class LevelSelectState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game, "levelselect")
        center_x = self.game.screen_width / 2 - (33 * 2) / 2
        center_y = self.game.screen_height / 2 - (33 * 2) / 2
        self.level_1_button = Button.LevelSelectButton(game, "Resources/Buttons/LevelSelect1.png", game.levels[0])
        self.level_1_button.SetPosition(0, center_y)
        self.level_2_button = Button.LevelSelectButton(game, "Resources/Buttons/LevelSelect2.png", game.levels[1])
        self.level_2_button.SetPosition(center_x / 2, center_y)
        self.level_3_button = Button.LevelSelectButton(game, "Resources/Buttons/LevelSelect3.png", game.levels[2])
        self.level_3_button.SetPosition(center_x, center_y)
        self.level_4_button = Button.LevelSelectButton(game, "Resources/Buttons/LevelSelect4.png", game.levels[3])
        self.level_4_button.SetPosition(center_x + center_x / 2, center_y)
        self.level_s_button = Button.LevelSelectButton(game, "Resources/Buttons/LevelSelectS.png", game.levels[4])
        self.level_s_button.SetPosition(self.game.screen_width - (33 * 2), center_y)
        self.back_button = Button.BackButton(game)
        self.back_button.SetPosition(self.game.screen_width / 2 - self.back_button.rect.width / 2, self.game.screen_height - self.back_button.rect.height)
        self.buttons = [self.level_1_button, self.level_2_button, self.level_3_button,
                        self.level_4_button, self.level_s_button, self.back_button]

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
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
            self.game.screen.blit(button. image, button.rect)
