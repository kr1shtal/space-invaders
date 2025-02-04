import time

import pygame
from bullet import Bullet
from crab import Crab


def update(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_d:
                ship.move_right = True
            if event.key == pygame.K_a:
                ship.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.move_right = False
            if event.key == pygame.K_a:
                ship.move_left = False


def refresh(bg_color, screen, ship, crabs, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.render()
    crabs.draw(screen)
    pygame.display.flip()


def update_bullets(screen, crabs, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, crabs, True, True)
    if len(crabs) == 0:
        bullets.empty()
        create_army(screen, crabs)


def move_crab(stats, screen, ship, crabs, bullets):
    crabs.update()
    if pygame.sprite.spritecollideany(ship, crabs):
        ship_death(stats, screen, ship, crabs, bullets)
    crabs_check(stats, screen, ship, crabs, bullets)


def ship_death(stats, screen, ship, crabs, bullets):
    stats.ship_life -= 1
    crabs.empty()
    bullets.empty()
    create_army(screen, crabs)
    ship.create_ship()
    time.sleep(1)


def crabs_check(stats, screen, ship, crabs, bullets):
    screen_rect = screen.get_rect()
    for crab in crabs.sprites():
        if crab.rect.bottom >= screen_rect.bottom:
            ship_death(stats, screen, ship, crabs, bullets)
            break


def create_army(screen, crabs):
    crab = Crab(screen)

    crabs_in_row = int(224 * 2 / 64)
    crabs_in_col = int(256 * 2 / 2 / 64)

    for col in range(crabs_in_col):
        for row in range(crabs_in_row):
            crab = Crab(screen)
            crab.x = crab.rect.width * row
            crab.y = crab.rect.height * col
            crab.rect.x = crab.x
            crab.rect.y = crab.rect.height + crab.rect.height * crabs_in_col
            crabs.add(crab)
