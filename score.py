import pygame
from pygame.sprite import Group
from ship import Ship


class Score:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = "white"
        self.font = pygame.font.Font(None, 24)
        self.draw_score()
        self.draw_high_score()
        self.draw_ship()

    def draw_high_score(self):
        self.high_score_image = self.font.render(
            str(self.stats.high_score), True, self.text_color
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def draw_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color)
        self.score_rect = self.score_img.get_rect()

    def draw_ship(self):
        self.ships = Group()
        for s in range(self.stats.ship_life):
            heart = Ship(self.screen)
            heart.image = pygame.image.load("res/heart.png")
            heart.rect.x = s * heart.rect.width
            heart.rect.y = 10
            self.ships.add(heart)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
