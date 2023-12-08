import pygame
import setup


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.state = 'inactive'
        self.image_addr = setup.Image_addr_laser
        self.image = pygame.image.load(self.image_addr)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = setup.dino_pos + 5, setup.dino_height - 30

    def update(self):
        if self.state == 'active':
            self.rect.left += setup.Going_speed
        if self.rect.left > 1280:
            self.rect.left = setup.dino_pos + 5
            self.state = 'inactive'

    def draw(self, screen):
        if self.state == 'active':
            screen.blit(self.image, self.rect)

    def active(self):
        self.state = 'active'

