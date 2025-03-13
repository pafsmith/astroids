import pygame
from constants import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")  # Or (0, 0, 0)

        pygame.display.flip()


if __name__ == "__main__":
    main()
