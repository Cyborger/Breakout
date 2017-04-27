import GameState
import Button

class LevelSelectState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game, "levelselect")
        self.level_1_button = Button.LevelSelectButton(game, "Resources/LevelSelect1.png", game.levels[0])
        self.level_1_button.SetPosition(0, 0)
        self.level_2_button = Button.LevelSelectButton(game, "Resources/LevelSelect2.png", game.levels[1])
        self.level_2_button.SetPosition(75, 0)
        self.level_3_button = Button.LevelSelectButton(game, "Resources/LevelSelect3.png", game.levels[2])
        self.level_3_button.SetPosition(150, 0)
        self.level_4_button = Button.LevelSelectButton(game, "Resources/LevelSelect4.png", game.levels[3])
        self.level_4_button.SetPosition(225, 0)
        self.level_s_button = Button.LevelSelectButton(game, "Resources/LevelSelectS.png", game.levels[4])
        self.level_s_button.SetPosition(300, 0)
        self.back_button = Button.BackButton(game)
        self.buttons = [self.level_1_button, self.level_2_button, self.level_3_button,
                        self.level_4_button, self.level_s_button]

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
