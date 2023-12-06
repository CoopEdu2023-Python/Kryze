import pygame


class Ground:

    def __init__(self):
        self.image_addr = str()
        self.rect = pygame.rect.Rect
        self.rect_next = pygame.rect.Rect
        self.image = pygame.surface.Surface
        self.image_next = pygame.surface.Surface
        self.background = pygame.surface.Surface

    def load(self):
        self.image = pygame.image.load(self.image_addr)
        self.image_next = self.image

    def update(self):
        self.background.fill("White")
        self.background.blit(self.image, self.rect)
        self.background.blit(self.image_next, self.rect_next)
        self.rect.left -= 10
        self.rect_next.left -= 10
        if self.rect.right <= 0:
            self.rect.left = self.rect_next.right
        if self.rect_next.right <= 0:
            self.rect_next.left = self.rect.right


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