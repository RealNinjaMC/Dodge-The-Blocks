import pygame
from game import Game
from settings import WIDTH, HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
font_big = pygame.font.SysFont("arial", 50)
font_small = pygame.font.SysFont("arial", 26)

def draw_menu():
    while True:
        window.fill((20, 20, 20))

        title = font_big.render("Dodge The Blocks", True, (0, 150, 255))
        play = font_small.render("Press SPACE to Play", True, (255, 255, 255))
        quit_msg = font_small.render("Press Q to Quit", True, (200, 200, 200))

        window.blit(title, (95, 200))
        window.blit(play, (155, 290))
        window.blit(quit_msg, (175, 330))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

def game_over_screen(score):
    while True:
        window.fill((0, 0, 0))

        text1 = font_big.render("GAME OVER", True, (255, 50, 50))
        text2 = font_small.render(f"Score: {score}", True, (255, 255, 255))
        text3 = font_small.render("Press SPACE to return to Menu", True, (180, 180, 180))

        window.blit(text1, (140, 200))
        window.blit(text2, (200, 270))
        window.blit(text3, (100, 330))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return

def main():
    while True:
        draw_menu()
        game = Game()
        alive = game.run()
        game_over_screen(game.score)

if __name__ == "__main__":
    main()
