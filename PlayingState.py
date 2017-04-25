import GameState
import Paddle
import Ball
import Timer

class PlayingState(GameState.GameState):
    def __init__(self, game, level):
        self.name = "playing"
        self.game = game
        self.paddle = Paddle.Paddle()
        starting_ball = Ball.Ball(200, 300)
        self.balls = [starting_ball]
        self.current_level = level
        self.current_level.ResetLevel()
        self.wait_for_start = Timer.Timer(100)

    def Update(self):  # Update paddle and ball
        self.wait_for_start.Update()
        if self.wait_for_start.complete:
            # Update paddle
            self.paddle.UpdateMovement()
            self.paddle.CheckOutOfBoundry(self.current_level.width, self.current_level.height)
            # Update balls
            for ball in self.balls:
                possible_collisions = self.current_level.blocks + [self.paddle]
                ball.UpdateMovement(possible_collisions)
                ball.CheckForOutOfBoundry(self.current_level.width, self.current_level.height)
            # Update blocks
            self.current_level.UpdateBlocks()
        self.RemoveLostBalls()


    def DrawScreen(self):  # Draw paddle, ball, bricks
        self.game.screen.blit(self.paddle.image, self.paddle.rect)
        for ball in self.balls:
            self.game.screen.blit(ball.image, ball.rect)
        for block in self.current_level.blocks:
            self.game.screen.blit(block.image, block.rect)

    def RemoveLostBalls(self):
        for ball in self.balls:
            if ball.rect.top >= self.game.screen_height:
                self.balls.remove(ball)

        if len(self.balls) == 0:
            self.game.GameOver()
