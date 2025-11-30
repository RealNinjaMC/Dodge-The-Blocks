import pygame
from settings import WIDTH, PLAYER_SIZE, PLAYER_SPEED

class Player: # player class to handle player properties and movement
    def __init__(self):
        x = WIDTH // 2 - PLAYER_SIZE // 2
        self.rect = pygame.Rect(x, 520, PLAYER_SIZE, PLAYER_SIZE)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += PLAYER_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 150, 255), self.rect) # blue = player
