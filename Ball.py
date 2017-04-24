import pygame
import Block

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Resources/Ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.move_x = 0.0
        self.move_y = 0.0
        self.base_speed = 3.0
        self.x_speed = self.base_speed
        self.y_speed = self.base_speed
        self.rect.x = 200.0
        self.rect.y = 300.0

    def UpdateMovement(self, collisions):  # Move at a constant speed
        self.move_x = 0.0
        self.move_y = 0.0
        self.move_x += self.x_speed
        self.move_y += self.y_speed
        self.CheckForCollision(collisions)

    def CheckForCollision(self, collisions):  # Check if it hits a block or the Paddle
        self.rect.y += self.move_y
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collide in collisions:
            if self.move_y > 0.0:
                self.rect.bottom = collide.rect.top
            elif self.move_y < 0.0:
                self.rect.top = collide.rect.bottom
            if isinstance(collide, Block.Block):
                collide.Break()
                
        if collisions:
            self.InvertYSpeed()

        self.rect.x += self.move_x
        collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collide in collisions:
            if self.move_x > 0.0:
                self.rect.right = collide.rect.left
            elif self.move_x < 0.0:
                self.rect.left = collide.rect.right
        if collisions:
            self.InvertXSpeed()

    def CheckForOutOfBoundry(self, level_width, level_height):  # Make sure it doesn't go off screen, except for bottom side
        if self.rect.right > level_width:
            self.rect.right = level_width
            self.InvertXSpeed()
        elif self.rect.left < 0:
            self.rect.left = 0
            self.InvertXSpeed()

        if self.rect.top < 0:
            self.rect.top = 0
            self.InvertYSpeed()

    def InvertXSpeed(self):
        self.x_speed *= -1.0

    def InvertYSpeed(self):
        self.y_speed *= -1.0
