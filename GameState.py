import pygame

class GameState:
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.mouse_pos = None


    def GetMousePos(self):
        raw_mouse_pos = pygame.mouse.get_pos()
        width_modifier = self.game.screen_width / self.game.display_info.current_w
        height_modifier = self.game.screen_height / self.game.display_info.current_h
        x = raw_mouse_pos[0] * width_modifier
        y = raw_mouse_pos[1] * height_modifier
        self.mouse_pos = [x, y]

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
        self.game.draw_screen.blit(pygame.transform.scale(self.game.screen, (self.game.display_info.current_w, self.game.display_info.current_h)), (0, 0))
        pygame.display.flip()
