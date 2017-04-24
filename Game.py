import StartMenuState
import PlayingState
import Level
import pygame

class Game:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.states = []
        self.current_state = None
        self.running = True
        level_1 = Level.Level("Resources/TestLevel.tmx")
        level_1.CreateLevel()
        self.levels = [level_1]
        self.clock = pygame.time.Clock()

    def Start(self):  # Set starting menu and stuff
        start_menu_state = StartMenuState.StartMenuState(self)
        self.NewState(start_menu_state)
        self.GameLoop()

    def StartPlaying(self):
        playing_state = PlayingState.PlayingState(self)
        playing_state.current_level = self.levels[0]
        self.NewState(playing_state)

    def ContinuePlaying(self):
        self.ChangeState(self.FindState("playing"))

    def ChangeState(self, state):  # See if state exists in states and act accordingly
        self.current_state = state

    def RemoveState(self, state):  # Remove state from states
        self.states.remove(state)

    def NewState(self, state):  # Add state to states and set to current
        self.states.append(state)
        self.current_state = state

    def FindState(self, name):
        for state in self.states:
            if state.name == name:
                return state

    def GameLoop(self):
        while self.running:
            self.current_state.HandleEvents(self)
            self.current_state.Update()
            self.current_state.ClearScreen(self.screen)
            self.current_state.DrawScreen(self.screen)
            self.current_state.UpdateDisplay()
            self.clock.tick(60)
