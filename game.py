import controls
import pygame
from pygame.sprite import Group
from ship import Ship


def run():
    pygame.init()

    WIDTH = 224
    HEIGHT = 256

    running = True

    window = pygame.display.set_mode((WIDTH * 2, HEIGHT * 2))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(window)
    bullets = Group()
    crabs = Group()

    controls.create_army(window, crabs)

    while running:
        controls.update(window, ship, bullets)
        ship.update()

        controls.refresh("black", window, ship, crabs, bullets)
        controls.update_bullets(bullets)
        controls.move_crab(crabs)


run()
