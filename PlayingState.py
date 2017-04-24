import GameState
import Paddle
import Ball

class PlayingState(GameState.GameState):
    def __init__(self, game):
        self.name = "playing"
        self.game = game
        self.paddle = Paddle.Paddle()
        starting_ball = Ball.Ball()
        self.balls = [starting_ball]
        self.current_level = None

    def Update(self):  # Update paddle and ball
        self.paddle.UpdateMovement()
        self.paddle.CheckOutOfBoundry(self.current_level.width, self.current_level.height)
        for ball in self.balls:
            possible_collisions = self.current_level.blocks + [self.paddle]
            ball.UpdateMovement(possible_collisions)
            ball.CheckForOutOfBoundry(self.current_level.width, self.current_level.height)
        self.current_level.RemoveDestroyedBlocks()


    def DrawScreen(self, screen):  # Draw paddle, ball, bricks
        screen.blit(self.paddle.image, self.paddle.rect)
        for ball in self.balls:
            screen.blit(ball.image, ball.rect)
        for block in self.current_level.blocks:
            screen.blit(block.image, block.rect)
