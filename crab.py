import pygame


class Crab(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Crab, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("res/crab.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x  # cast to float
        self.y = self.rect.y

    def render(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.1
        self.rect.y = self.y
