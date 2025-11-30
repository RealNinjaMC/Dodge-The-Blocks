import pygame
import random
import os

from player import Player
from enemy import Enemy
from settings import (
    WIDTH, HEIGHT, FPS,
    INITIAL_ENEMY_SPEED, INITIAL_SPAWN_RATE,
    HIGHSCORE_FILE
)

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge The Blocks")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 28)

        self.highscore = self.load_highscore()
        self.reset()

    def load_highscore(self):
        if not os.path.exists(HIGHSCORE_FILE):
            return 0
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0

    def save_highscore(self):
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(self.highscore))

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
                self.player.take_damage()
                self.enemies.remove(enemy)
                if self.player.health <= 0:
                    return False
        return True

    def increase_difficulty(self):
        self.difficulty_timer += 1
        if self.difficulty_timer % (FPS * 10) == 0:
            self.enemy_speed += 1
            if self.spawn_rate > 8:
                self.spawn_rate -= 1

    def draw_health(self):
        for i in range(self.player.health):
            pygame.draw.rect(self.window, (0, 255, 0), (10 + i * 25, 50, 20, 20))

    def draw(self):
        self.window.fill((25, 25, 25))

        self.player.draw(self.window)

        for enemy in self.enemies:
            enemy.draw(self.window)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        hs_text = self.font.render(f"High Score: {self.highscore}", True, (200, 200, 200))

        self.window.blit(score_text, (10, 10))
        self.window.blit(hs_text, (WIDTH - 220, 10))

        self.draw_health()

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
                if self.score > self.highscore:
                    self.highscore = self.score
                    self.save_highscore()
                return False

            self.score += 1
            self.increase_difficulty()
            self.draw()

        return False
