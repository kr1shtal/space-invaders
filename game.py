import controls
import pygame
from pygame.sprite import Group
from score import Score
from ship import Ship
from stats import Stats


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
    stats = Stats()
    sc = Score(window, stats)

    controls.create_army(window, crabs)

    while running:
        controls.update(window, ship, bullets)
        if stats.run_game:
            ship.update()
            controls.refresh("black", window, stats, sc, ship, crabs, bullets)
            controls.update_bullets(window, stats, sc, crabs, bullets)
            controls.move_crab(stats, window, sc, ship, crabs, bullets)


run()
