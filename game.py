import pygame
import random

from player import Player
from enemy import Enemy
from settings import (
    WIDTH, HEIGHT, FPS,
    INITIAL_ENEMY_SPEED, INITIAL_SPAWN_RATE
)

class Game: # game class to handle game logic
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge The Blocks")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 28)

        self.reset()

    def reset(self):
        self.player = Player()
        self.enemies = []
        self.score = 0

        self.enemy_speed = INITIAL_ENEMY_SPEED
        self.spawn_rate = INITIAL_SPAWN_RATE
        self.difficulty_timer = 0

    def spawn_enemy(self):
        self.enemies.append(Enemy())

    def update_enemies(self):
        for enemy in self.enemies[:]:
            enemy.update(self.enemy_speed)

            if enemy.rect.y > HEIGHT:
                self.enemies.remove(enemy)

            if self.player.rect.colliderect(enemy.rect):
                return False  # collision detected = game over 
        return True

    def increase_difficulty(self):
        self.difficulty_timer += 1
        if self.difficulty_timer % (FPS * 10) == 0:
            self.enemy_speed += 1
            if self.spawn_rate > 8:
                self.spawn_rate -= 1

    def draw(self):
        self.window.fill((25, 25, 25))

        self.player.draw(self.window)

        for enemy in self.enemies:
            enemy.draw(self.window)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

        pygame.display.update()

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            if random.randint(1, self.spawn_rate) == 1:
                self.spawn_enemy()

            if not self.update_enemies():
                return False  # lose the game

            self.score += 1
            self.increase_difficulty()
            self.draw()

        return False
