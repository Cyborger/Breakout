import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Resources/Paddle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 600
        self.move_speed = 4.0

    def UpdateMovement(self):  # Check for movement and stuff
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.move_speed

    def CheckOutOfBoundry(self, level_width, level_height):  # Make sure the paddle doesnt go off the screen
        if self.rect.right > level_width:
            self.rect.right = level_width
        elif self.rect.x < 0:
            self.rect.left = 0
