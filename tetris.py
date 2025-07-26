import pygame, sys
from game import Game

pygame.init()
WINDOW_WIDTH= 300
WINDOW_HEIGHT = 600
DARK_BLUE = (44, 44, 127)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python tetris - Version 0.1")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()

    #Drawing
    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)