import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
user_image = pygame.image.load("test.png")
screen.blit(user_image, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print("X: ", x, " | ", "Y: ", y)

    pygame.display.update()