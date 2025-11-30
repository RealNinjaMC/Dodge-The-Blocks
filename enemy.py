import pygame
import random
from settings import WIDTH, ENEMY_SIZE

class Enemy: # enemy class to handle enemy properties and movement
    def __init__(self):
        x = random.randint(0, WIDTH - ENEMY_SIZE) # spawn at random x position
        self.rect = pygame.Rect(x, -40, ENEMY_SIZE, ENEMY_SIZE) # start above the screen

    def update(self, speed): 
        self.rect.y += speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 60, 60), self.rect) # RED BLOCK (enemy)
