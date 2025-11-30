import pygame
from game import Game
from settings import WIDTH, HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
font_big = pygame.font.SysFont("arial", 50)
font_small = pygame.font.SysFont("arial", 26)

def game_over_screen(score): # display game over and final score
    while True:
        window.fill((0, 0, 0))
 
        text1 = font_big.render("GAME OVER", True, (255, 50, 50)) 
        text2 = font_small.render(f"Score: {score}", True, (255, 255, 255))
        text3 = font_small.render("Press SPACE to restart", True, (180, 180, 180))

        window.blit(text1, (140, 200))
        window.blit(text2, (200, 270))
        window.blit(text3, (135, 330))

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
        game = Game()
        alive = game.run()

        game_over_screen(game.score)

if __name__ == "__main__":
    main()
