import pygame
import setup


class Ground:

    def __init__(self):
        self.image_addr = setup.Image_addr_background
        self.rect = pygame.rect.Rect
        self.rect_next = pygame.rect.Rect
        self.image = pygame.surface.Surface
        self.image_next = pygame.surface.Surface
        self.speed = 5

    def load(self):
        self.image = pygame.image.load(self.image_addr)
        self.image_next = self.image
        self.rect = self.image.get_rect()
        self.rect_next = self.image_next.get_rect()
        self.rect.left, self.rect.bottom = 0, setup.Ground_height
        self.rect_next.left = self.rect.width
        self.rect_next.bottom = setup.Ground_height

    def update(self):
        self.rect.left -= self.speed
        self.rect_next.left -= self.speed
        if self.rect.right <= 0:
            self.rect.left = self.rect_next.right
        if self.rect_next.right <= 0:
            self.rect_next.left = self.rect.right

    def draw(self, background):
        background.fill("White")
        background.blit(self.image, self.rect)
        background.blit(self.image_next, self.rect_next)


class Moon:
    pass


class Cloud:
    pass


class Star:
    pass


class Scoreboard:
    pass


class EndingIcon:
    pass