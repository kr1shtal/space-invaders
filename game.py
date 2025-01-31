import pygame
import controls
from ship import Ship


def run():
    pygame.init()

    WIDTH = 224
    HEIGHT = 256

    running = True

    window = pygame.display.set_mode((WIDTH * 2, HEIGHT * 2))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(window)

    while running:
        controls.update(ship)
        ship.update()

        window.fill("black")
        ship.render()
        pygame.display.flip()


run()
