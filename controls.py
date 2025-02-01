import pygame
from bullet import Bullet


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


def refresh(bg_color, screen, ship, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.render()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
