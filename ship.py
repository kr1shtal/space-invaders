import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("res/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def render(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1

    def update_screen(bg_color, screen, ship):
        screen.fill(bg_color)
        ship.render()
        pygame.display.flip()
