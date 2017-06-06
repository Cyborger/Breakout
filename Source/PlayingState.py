import GameState
import Paddle
import Ball
import Timer
import pygame

class PlayingState(GameState.GameState):
    def __init__(self, game, level):
        super().__init__(game, "playing")

        self.paddle = Paddle.Paddle()
        starting_ball = Ball.Ball(0, 0)
        if level.ball_x is None and level.ball_y is None:
            starting_ball.rect.centerx = self.paddle.rect.centerx
            starting_ball.rect.bottom = self.paddle.rect.top
        else:
            starting_ball.rect.x = level.ball_x
            starting_ball.rect.y = level.ball_y
        self.balls = [starting_ball]
        self.current_level = level
        self.current_level.ResetLevel()
        self.wait_for_start = Timer.Timer(100)

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
                elif event.key == pygame.K_ESCAPE:
                    self.game.Pause()

    def Update(self):  # Update paddle and ball
        self.wait_for_start.Update()
        if self.wait_for_start.complete:
            # Update paddle
            self.paddle.UpdateMovement(self.balls)
            self.paddle.CheckOutOfBoundry(self.current_level.width, self.current_level.height)
            # Update balls
            for ball in self.balls:
                possible_collisions = self.current_level.blocks + [self.paddle]
                ball.UpdateMovement(possible_collisions)
                ball.CheckForOutOfBoundry(self.current_level.width, self.current_level.height)
            # Update blocks
            self.current_level.UpdateBlocks()
        self.CheckForWin()
        self.RemoveLostBalls()


    def DrawScreen(self):  # Draw paddle, ball, bricks
        self.game.screen.blit(self.paddle.image, self.paddle.rect)
        for ball in self.balls:
            self.game.screen.blit(ball.image, ball.rect)
        for block in self.current_level.blocks:
            self.game.screen.blit(block.image, block.rect)

    def CheckForWin(self):
        if len(self.current_level.blocks) == 0:
            self.game.LevelComplete()
            self.game.level_complete_music.play()

    def RemoveLostBalls(self):
        for ball in self.balls:
            if ball.rect.top >= self.game.screen_height:
                self.balls.remove(ball)

        if len(self.balls) == 0:
            self.game.GameOver()
            self.game.gameover_music.play()
