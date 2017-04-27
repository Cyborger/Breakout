import pygame
import Block
import Paddle
import random
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        self.image = pygame.image.load("Resources/Ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.move_x = 0.0
        self.move_y = 0.0
        self.base_speed = 6.0
        self.current_speed = self.base_speed
        self.x_speed = self.current_speed / 2.0
        self.y_speed = self.GetCorrespondingY()
        self.rect.x = x
        self.rect.y = y
        random.seed()

    def UpdateMovement(self, collisions):  # Move at a constant speed
        self.move_x = 0.0
        self.move_y = 0.0
        self.move_x += self.x_speed
        self.CheckForHorizontalCollision(collisions)
        self.move_y += self.y_speed
        self.CheckForVerticalCollision(collisions)

    def CheckForHorizontalCollision(self, collisions):  # Check if it hits a block or the Paddle
        self.rect.x += self.move_x
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collide in collisions:
            if self.move_x > 0.0:
                self.rect.right = collide.rect.left
            elif self.move_x < 0.0:
                self.rect.left = collide.rect.right
            if isinstance(collide, Block.Block):
                collide.Hit()
        if collisions:
            self.InvertXSpeed()

    def CheckForVerticalCollision(self, collisions):
        self.rect.y += self.move_y
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collide in collisions:
            if self.move_y > 0.0:
                self.rect.bottom = collide.rect.top
            elif self.move_y < 0.0:
                self.rect.top = collide.rect.bottom
            if isinstance(collide, Block.Block):
                collide.Hit()
            elif isinstance(collide, Paddle.Paddle):
                self.RandomBounce()
        if collisions:
            self.InvertYSpeed()

    def CheckForOutOfBoundry(self, level_width, level_height, no_bottom = True):  # Make sure it doesn't go off screen, except for bottom side
        if self.rect.right >= level_width:
            self.rect.right = level_width
            self.InvertXSpeed()
        elif self.rect.x < 0:
            self.rect.x = 0
            self.InvertXSpeed()

        if self.rect.top <= 0:
            self.rect.top = 0
            self.InvertYSpeed()

        if not no_bottom:
            if self.rect.bottom >= level_height:
                self.rect.bottom = level_height
                self.InvertYSpeed()

    def RandomBounce(self):
        negative_random = random.randint(-self.current_speed + 1, -1)
        positive_random = random.randint(1, self.current_speed - 1)
        choice = random.randint(0, 1)
        if choice == 0:
            self.x_speed = negative_random
        else:
            self.x_speed = positive_random
        self.y_speed = self.GetCorrespondingY()

    def GetCorrespondingY(self):
        new_y = int(math.sqrt(self.current_speed**2 - self.x_speed**2))
        return new_y

    def InvertXSpeed(self):
        self.x_speed *= -1.0

    def InvertYSpeed(self):
        self.y_speed *= -1.0
