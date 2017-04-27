import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Resources/Paddle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 720 / 2
        self.rect.y = 350
        self.move_speed = 6.0

    def UpdateMovement(self, collisions):  # Check for movement and stuff
        move_amount = 0
        if (pygame.key.get_pressed()[pygame.K_LEFT]
        or pygame.mouse.get_pressed()[0]
        or pygame.key.get_pressed()[pygame.K_a]):
            move_amount -= self.move_speed
        if (pygame.key.get_pressed()[pygame.K_RIGHT]
        or pygame.mouse.get_pressed()[2]
        or pygame.key.get_pressed()[pygame.K_d]):
            move_amount += self.move_speed

        self.rect.x += move_amount
        ball_collides = pygame.sprite.spritecollide(self, collisions, False)
        for ball in ball_collides:
            if move_amount > 0:
                ball.rect.left = self.rect.right
            elif move_amount < 0:
                ball.rect.right = self.rect.left

    def CheckOutOfBoundry(self, level_width, level_height):  # Make sure the paddle doesnt go off the screen
        if self.rect.right > level_width:
            self.rect.right = level_width
        elif self.rect.x < 0:
            self.rect.left = 0
